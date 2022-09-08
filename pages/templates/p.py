#!/usr/bin/python3

import sys

lines=open('index.html.source','r').readlines()

#print(lines[0])

#sys.exit()

filelines=[]

for line in lines:
	# make the lines the same as for the source 
	# print(repr(line))
	linewithcarriagereturn=str.replace(line, '\n', '\r\n')
	filelines.append(linewithcarriagereturn)
	# print(repr(linewithcarriagereturn))


fd=open('index.html','w')

fd.writelines(filelines)

fd.close()


"""
$ is enter
^M is carriage return

head -n1 index.html.source|cat -te
<!DOCTYPE html>^M$

 head -n1 index.html|cat -te
<!DOCTYPE html>^M$

