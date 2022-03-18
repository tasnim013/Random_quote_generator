from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

# Function to get clean content

def clean_text(x):
    
    temp=str(x)
    
    temp_split=temp.split(".",maxsplit=2)
    text=temp_split[0][2:]
    author=temp_split[-1][1:-2]
    
    return text,author

# Source url

url="https://louisem.com/63350/best-motivational-quotes"

# Make Soup!

r=requests.get(url)

soup=BeautifulSoup(r.text,"html.parser") #get soup object

# Find content

cont=soup.find_all(lambda tag: tag.name == 'p' and not tag.attrs)


quotes=[]
for i in range(10,160):
    if "<" not in str(cont[i].contents):
        text,author =clean_text(x=cont[i].contents)
        
        if len(author)<23:
            quotes.append((text,author))
        


# Build a datafile

df= pd.DataFrame(quotes, columns=["Quote","Author"])

df.head()

# Exporting the dataset to a json file

data=df.to_json(orient="records")
result=json.loads(data)

with open('motivational_data.js', 'w') as outfile:
    json.dump(result, outfile,indent=4)

