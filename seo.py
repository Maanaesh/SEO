import requests
import re
from bs4 import BeautifulSoup

url=input("Enter A url:")
key=input("Enter the word to lookup:")
r=requests.get(url)
c=r.text
h=re.findall(key,c)
print("The Word ",key,"Has Occured ",len(h),"times in ",url)
