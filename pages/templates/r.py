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
last=occurances[1]

u=t[:first]

print(repr(u))

au=t[:first]+'"{%'

print(repr(au))


