#!/usr/bin/python3

import re

occurances=[m.start() for m in re.finditer('test', 'test test test test')]

print(occurances)

t='''<script src="js/jquery-1.11.0.min.js"></script>'''

print(t)

# find string occurances maybe later only find first or last ones

occurances=[m.start() for m in re.finditer('"', t)]

print(occurances)



first=occurances[0]
second=occurances[1]
aftersecond=occurances[1]+1

u=t[:first]

print(repr(u))

au=t[:first]+'"{% static '

print(repr(au))


au2=au+t[first:second+1]

print(repr(au2))

au3=au2+t[second+1:]

print(repr(au3))
