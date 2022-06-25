#!/usr/bin/python3
"""
This is to convert a html file to one that can be put in static location of django like with white noise. It should not
effect external links ony internal ones and should follow convention fron about file

Before any changes this print all works with same sum as

"""
#print('{% load static %}')
lines=open('demolition1.html.source').readlines()
#html_doc=''.join(lines)

def get_all():
    for l in lines:
        print(l,end='')

def update_img():
    #  <img src = "imagest/image0-800.jpg">
    # ['      <a class="navbar-brand" href="index.html"></a>', '="jmb.png">\n']

for l in lines:
    if 'img src =' in