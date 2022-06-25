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
        if '<img' in l:
            lettersinline=[]
            pastImageTag=False
            for letter in l:
                lettersinline.append(letter)
            print(lettersinline)
            print('These should be the same')
            combined=''.join(lettersinline)
            print(combined)
            print(combined == l)
            print( lettersinline[-3:] )
            #if lettersinline[-3:]= ['i', 'm', 'g']:
            #    pastImageTag=True
            #if pastIma
            break

#update_img()

line=[' ', ' ', ' ', ' ', ' ', ' ', '<', 'a', ' ', 'c', 'l', 'a', 's', 's', '=', '"', 'n', 'a', 'v', 'b', 'a', 'r', '-', 'b', 'r', 'a', 'n', 'd', '"', ' ', 'h', 'r', 'e', 'f', '=', '"', 'i', 'n', 'd', 'e', 'x', '.', 'h', 't', 'm', 'l', '"', '>', '<', '/', 'a', '>', '<', 'i', 'm', 'g', ' ', 's', 'r', 'c', '=', '"', 'j', 'm', 'b', '.', 'p', 'n', 'g', '"', '>', '\n']


def updateline(line):
    lettersinline=[]
    pastImageTag=False
    pastSourceTag=False
    pastEquals=False
    startindexchange=False
    stopindexchange=False

    # needed so a break can still now so scroll through rest of letters knowing the img
    # tag has been found

    for letter in line:
        lettersinline.append(letter)
        if lettersinline[-3:] == ['i', 'm', 'g']:
            pastImageTag=True
            print(lettersinline)
        if pastImageTag:
            if lettersinline[-3:] == ['s', 'r', 'c']:
                pastSourceTag = True
                print(lettersinline)

        if pastSourceTag:
            if lettersinline[-1] == '=':
                pastEquals=True
                print(lettersinline)

       # this o
        if pastEquals and not stopindexchange:
           if lettersinline[-1] == '"':
                # take away one so it is the index
                startindexchange=len(lettersinline)-1
                print(startindexchange)

        if startindexchange and stopindexchange:
            if lettersinline[-1] == '"':
                # take away one so it is the index
                stopindexchange=len(lettersinline)-1
                print(stopindechange)


    #
    # todo get index of appended list


        #todo capture index of speech signs then inject into middle
        #todo  turn this rep into function

#for l in lines[0]:
#    print(''.join(l))
#    updateline(l)

#updateline(line)


#todo inject into list a string bigger than original



def updateplace(list1, startindex, endindex, value='bam'):
    listcopy=list(list1)
    newlist=[]
    replacing=False
    for i in listcopy:
        #breakpoint()
        if not replacing: newlist.append(i)
        #(len(listcopy)-1, startindex)
        if len(newlist)-1 == startindex:
            replacing=True
            for x in list(value):
                newlist.append(x)

        if len(newlist)-1 == endindex:
            replacing=False

    return newlist









print ( updateplace([0,1,2,3,4,5,6,7], 2,4) )
