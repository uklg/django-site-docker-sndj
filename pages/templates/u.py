#!/usr/bin/python3


u='a dog called paul walked there'

print('before')
print(repr(u))


matchstring='paul'
index=u.find(matchstring)
lastindex=index+(len(matchstring))
newstring=u[:index]+'bob'+u[lastindex:]

print(matchstring,index,lastindex, newstring)


print('after')


print(repr(u))

"""
before
'a dog called paul walked there'
paul 13 17 a dog called bob walked there
after
'a dog called paul walked there'

"""

