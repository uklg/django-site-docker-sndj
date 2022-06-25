#!/usr/bin/python3

def getsendmailapikey():
	fd=open('sendgrid.env','r')
	keyline=fd.readlines()[0].strip()
	delimiter="'"

	splitkey=keyline.split(delimiter)
	keysection=splitkey[-2].strip()
	return(keysection)


print(getsendmailapikey())
