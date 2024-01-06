# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"

#1. get the html
r=requests.get(url)
htmlContent=r.content
# print(htmlContent)

# 2.parse the html
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)

# 3.html tree traversal


# commonly used types of objects:

# print(type(title))# 1.Tag

# print(type(title.string)) # 2.navigableString
# print(type(title))# 3.BeautifulSoup

# 4.comment
# markup="<p><!-- this is a comment --></p>"
# soup2=BeautifulSoup(markup)
# print(type(soup2.p.string))
# exit()

# get the title of the HTML page
title=soup.title

# get all the paragraphs from the page
paras=soup.find_all('p')
# print(paras)


# get first element in the HTML page
print(soup.find('p'))

# get classes of any element in the HTML page
print(soup.find('p')['class'])

# find all the elements with class lead
print(soup.find_all("p",class_="lead"))

# get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

# get all the a from the page
anchors=soup.find_all('a')
all_links=set()
# print(anchors)

# get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'):
        linkText="https://codewithharry.com" + link.get('href')
        all_links.add(link)
        print(linkText)
        
navbarSupportedContent = soup.find(id='navbarSupportedContent')

# .contents-A tag's children are available as a list
# .children -A tag's children are available as a generator
#  for elem in navbarSupportedContent.contents:
#       print(elem)

# for item in navbarSupportedContent.strings:
#     print(item)
    
    
# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# print(navbarSupportedContent.parent)
# for item in navbarSupportedContent.parents:
#     print(item.name)


elem=soup.select("#loginModal")
print(elem)