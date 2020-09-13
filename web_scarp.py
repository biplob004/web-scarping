
from bs4 import BeautifulSoup
import requests

url = 'http://example.com' # Here is full url of the page you want to scarp

r = requests.get(url) # request the page 

data = r.content # get content of the page

print(data)
print(r.status_code) # get status code, it may be: 404 if page not found and 200 if success, like so.
print(r.headers) # it returns headers of the request
print(r.apparent_encoding) # eg: ascii
print(r.cookies) # returns cookies
print(r.encoding) # eg: utf-8

soup = BeautifulSoup(data, 'lxml') # using BeautifulSoup, it will pretify your content and allows to use lots of functions

all_paragraphs = soup.find_all('p') # returns a list with html tag 'p'

for p in all_paragraphs:
    print(p.text) # .text will return the text only
    
    
print(soup.title.text) # title of webpage
print(soup.title.name) # returns html tag name
print(soup.title.parent.name) # returns parent tag name
print(soup.p)
print(soup.a['href']) # if not found it will throw an error
print(soup.a.get('href')) # if not found return will be None
print(soup.find_all('p'))
print(soup.find(id='any_id'))
print(soup.get_text()) # get all text from webpage
print(BeautifulSoup("<html><head></head><body>Hello there </body></html>")) # instead of link taking data from string 
print(soup.a.attrs) # returns dic of attributes
print(soup.select('h a')) # here select <a> of <h> 


