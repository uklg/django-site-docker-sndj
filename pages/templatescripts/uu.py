#!/usr/bin/python3
"""
This is to convert a html file to one that can be put in static location of django like with white noise. It should not
effect external links ony internal ones and should follow convention fron about file
"""
print('{% load static %}')
lines=open('demolition1.html.source').readlines()
#html_doc=''.join(lines)



for l in lines:
 #if '<img' in l:
    print(l,end='')



import sys

sys.exit





#print(html_doc)

#for l in lines:
#    print(l,end='')

# now the file has the same sum
#
# print
#for l in lines:
#    if 'href' in l:
 #       for
 #   print(l,end='')







#import lxml.html as LH
#root = LH.fromstring(html_string)
#for el in root.iter('img'):
#    el.attrib['src'] = 'new src'
#print(LH.tostring(root, pretty_print=True))

#from BeautifulSoup4 import BeautifulSoup
#soup = BeautifulSoup(html_string)
#for link in soup.findAll('a'):
#    link['src'] = 'New src'
#html_string = str(soup)

"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
for el in soup.find_all('img'):
    oldsource=el['src']
    parsed = str('"{% static'+' '+'"' +oldsource+'"'+ ' '+'%}"')
    #todo work out why extra quote that does not work properly single quote is ok
    el['src']=parsed[1:-1]
    #print(help(el))
    #print(el)


for el in soup.find_all('link'):
    oldsource=el['href']
    parsed = str('"{% static'+' '+'"' +oldsource+'"'+ ' '+'%}"')
    el['href']=parsed[1:-1]


for el in soup.find_all('script'):
    oldsource=el['src']
    parsed = str('"{% static'+' '+'"' +oldsource+'"'+ ' '+'%}"')
    el['src']=parsed[1:-1]

    #print(el)

print(soup.prettify())

#print(soup)

#  "{% static "dog.png" %}"


"""
