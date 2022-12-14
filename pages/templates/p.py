#!/usr/bin/python3

"""
This converts a html file to be compatible with static files and was used completely successfully to
produce index.html from index.html.source
"""


import sys,os,re

lines=open('index.html.source','r').readlines()

#print(lines[0])

#sys.exit()

filelines=[]
filelines=filelines+['''{% load static %}\n''']


def update_with_static(line,pattern='"',type='js'):
	t=line
	# find all string occurances
	# maybe later only find first or last ones
	occurances=[m.start() for m in re.finditer(pattern, t)]
	if type=='js':
		occurances=occurances[0:2]
	if type=='css':
		# ignore first set of speechmarks
		occurances=occurances[2:]

	if type=='jpg':
		# Only use the first set of speechmarks
 		occurances=occurances[0:2]


	first=occurances[0]
	second=occurances[1]
	aftersecond=occurances[1]+1
	u=t[:first]
	au=t[:first]+'"{% static '
	au2=au+t[first:second+1]
	au3=au2+'%}"'+t[second+1:]
	#print(repr(au3))
	return au3



for line in lines:
	# make the lines the same as for the source 
	# print(repr(line))
	if '.js' in line:
		line=update_with_static(line,type='js')
	if '.css' in line:
		line=update_with_static(line,type='css')
	if '.jpg' in line:
		line=update_with_static(line,type='jpg')

	linewithcarriagereturn=str.replace(line, '\n', '\r\n')
	filelines.append(linewithcarriagereturn)
	# print(repr(linewithcarriagereturn))


fd=open('index.html','w')

fd.writelines(filelines)

fd.close()

print('running diff on index.html and index.html.source')
os.system('diff index.html index.html.source')

"""
$ is enter
^M is carriage return

head -n1 index.html.source|cat -te
<!DOCTYPE html>^M$

 head -n1 index.html|cat -te
<!DOCTYPE html>^M$
"""


