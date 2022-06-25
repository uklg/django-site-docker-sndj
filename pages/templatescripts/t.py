#!/usr/bin/python3

lines=open('demolition1.html.source','r').readlines()

# <img src = "imagest/image0-800.jpg">


ss='img src'

for l in lines:
	if '<img' in l:
		#print(l)
		srcsplit=l.split(ss) 
		srcsplitl=l.split(ss)[0]
		srcsplitr=l.split(ss)[1]
		#print('W: ',srcsplitr)
		# W:   = "imagest/image0-800.jpg">
		rsplit=srcsplitr.split('"')


		#print(rsplit)

		# ['=', 'jmb.png', '>\n']
		oldurl=rsplit[1]
		#print(oldurl)
		parsed = str('{% static'+' '+'"' +oldurl+'"'+ ' '+'%}')
		#print(parsed)
		rsplit[1]=parsed
		newrsplit='"'.join(rsplit)
		#print(newrsplit)

            
		#print(l)
                # this may need a join for edgecases
		#print(srcsplitl+ss+srcsplitr)

		# files should be the same
		combined=srcsplitl+ss+srcsplitr
		#print(combined==l)


		#print(srcsplitl+ss+newrsplit,end='')

	#else: print(l,end='') 
