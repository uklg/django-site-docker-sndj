#!/usr/bin/python3

# This makes a static file ready to be a template and access static resouces dynamically set
# ./parsesite.py > demolition1.html.source.gen
# diff demolition1.html.source.gen demolition1.html.source|less 

lines=open('demolition1.html.source','r').readlines()

# <img src = "imagest/image0-800.jpg">


print('{% load static %}')

ss='img src'




for l in lines:
	if '<img' in l:
		# print(l) <a class="navbar-brand" href="index.html"></a><img src="jmb.png">
		srcsplit=l.split(ss) 
		srcsplitl=l.split(ss)[0]
		srcsplitr=l.split(ss)[1]
		#print('W: ',srcsplitr) # W:   = "imagest/image0-800.jpg">
		rsplit=srcsplitr.split('"')


		# print(rsplit) # [' = ', 'imagest/image0-800.jpg', '>\n']


		# ['=', 'jmb.png', '>\n']
		oldurl=rsplit[1]
		# print(oldurl) # [' = ', 'imagest/image0-800.jpg', '>\n']
		parsed = str('{% static'+' '+'"' +oldurl+'"'+ ' '+'%}')

		# print(parsed) # {% static "imagest/image0-800.jpg" %}

		rsplit[1]=parsed
		newrsplit='"'.join(rsplit)
		#print(newrsplit)

            
                # this may need a join for edgecases
		#print(srcsplitl+ss+srcsplitr)

		# files should be the same as no changes have been made
		combined=srcsplitl+ss+srcsplitr
		#print(combined==l)


		print(srcsplitl+ss+newrsplit,end='')



       else if link'


	else: print(l,end='') 
