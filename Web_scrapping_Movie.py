from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

# Function to get content

def get_content(x,tag=""):
    content=[]
    
    for t in x:
        temp=t.find(tag)
        if temp:
            content.append(temp.text)
    return content

# Source url

url="https://www.infoplease.com/culture-entertainment/film/top-100-movie-quotes"

# Make Soup!

r=requests.get(url)

soup=BeautifulSoup(r.text,"html.parser") #get soup object

# Find content

cont=soup.find_all(lambda tag: tag.name == 'p' and not tag.attrs)

quote=get_content(cont,tag="b") # scrap quote

author=get_content(cont,tag="em") #scrap author

#Delete extra headline
del(quote[0])

final_quotes=[]
for q,a in zip(quote,author):
    
    final_quotes.append((q[1:-1],a))

# Build a datafile

df= pd.DataFrame(final_quotes, columns=["Quote","Author"])

df.head()

# Exporting the dataset to a json file

data=df.to_json(orient="records")
result=json.loads(data)

with open('movie_data.js', 'w') as outfile:
    json.dump(result,outfile,indent=4)

