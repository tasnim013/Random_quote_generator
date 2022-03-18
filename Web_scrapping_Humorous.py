from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

# Source url

url="https://blog.vantagecircle.com/funny-work-quotes/"

# Make Soup!

r=requests.get(url)

soup=BeautifulSoup(r.text,"html.parser") #get soup object

# Find content

cont=soup.find_all(lambda tag: tag.name == 'blockquote' and not tag.attrs)

content=[]
for t in cont:
    temp=t.find("p").text
    content.append(temp)
    
#Delete unwanted text 
del(content[0])

final_quotes=[]

for c in content:
    temp=c.split("\n")
    
    # to avoid missing value
    if len(temp)>1:  
        quote=temp[0]
        author=temp[1]
        final_quotes.append((quote,author))
    

# Build a datafile

df= pd.DataFrame(final_quotes, columns=["Quote","Author"])

df.head()

# Exporting the dataset to a json file

data=df.to_json(orient="records")
result=json.loads(data)

with open('humorous_data.js', 'w') as outfile:
    json.dump(result,outfile,indent=4)

