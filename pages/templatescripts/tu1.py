#!/usr/bin/python3

lines=open('demolition1.html','r').readlines()

# <img src = "imagest/image0-800.jpg">


ss='img src'

for l in lines:
	if '<img' in l:
		#print(l)
		srcsplit=l.split(ss) 
		srcsplitl=l.split(ss)[0]
		srcsplitr=l.split(ss)[1]
            
		print(l)
		print(srcsplitl+ss+srcsplitr)

		# files should be the same
		combined=srcsplitl+ss+srcsplitr
		print(combined==l)



