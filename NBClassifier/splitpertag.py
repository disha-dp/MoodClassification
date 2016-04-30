# -*- coding: utf-8 -*-
import sys
import math
import os
import re
import string
import codecs
import numpy
import pickle
import ast

s=open('C:\\Users\\LENOVO\\PycharmProjects\\test\\hgm1.txt','r',encoding='utf8')
c=s.read()
diction= ast.literal_eval(c)

sadfile = open('sad.txt','w',encoding='utf8')
happyfile = open('happy.txt','w',encoding='utf8')
devotionalfile = open('devotional.txt','w',encoding='utf8')
patrioticfile = open('patriotic.txt','w',encoding='utf8')
funnyfile = open('funny.txt','w',encoding='utf8')
friendshipfile = open('friendship.txt','w',encoding='utf8')
romanticfile = open('romantic.txt','w',encoding='utf8')
partyfile = open('party.txt','w',encoding='utf8')
tareeffile = open('tareef.txt','w',encoding='utf8')
satirefile = open('satire.txt','w',encoding='utf8')
naughtyfile = open('naughty.txt','w',encoding='utf8')
playfulfile = open('playful.txt','w',encoding='utf8')
mastifile = open('masti.txt','w',encoding='utf8')
itemfile = open('item.txt','w',encoding='utf8')
rockfile = open('rock.txt','w',encoding='utf8')
popfile = open('pop.txt','w',encoding='utf8')
motivationalfile = open('motivational.txt','w',encoding='utf8')
remixfile = open('remix.txt','w',encoding='utf8')
lovefile = open('love.txt','w',encoding='utf8')
storyfile = open('story.txt','w',encoding='utf8')
dancefile = open('dance.txt','w',encoding='utf8')

for k,labels in diction.items():
    #label=labels.split('//')
    label = labels.split()[0].lower()
    label = labels.split('/')[0]
    delimiter = '\n-|\n'
    print (label)
    if 'sad' in label:
        sadfile.write(k)
        sadfile.write(delimiter)
    elif 'happy' in label:
        happyfile.write(k)
        happyfile.write(delimiter)
    elif 'devotional' in label:
        devotionalfile.write(k)
        devotionalfile.write(delimiter)
    elif 'patriotic' in label:
        patrioticfile.write(k)
        patrioticfile.write(delimiter)
    elif 'funny' in label:
        funnyfile.write(k)
        funnyfile.write(delimiter)
    elif 'friendship' in label:
        friendshipfile.write(k)
        friendshipfile.write(delimiter)
    elif 'romantic' in label:
        romanticfile.write(k)
        romanticfile.write(delimiter)
    elif 'party' in label:
        partyfile.write(k)
        partyfile.write(delimiter)
    elif 'tareef' in label:
        tareeffile.write(k)
        tareeffile.write(delimiter)
    elif 'satire' in label:
        satirefile.write(k)
        satirefile.write(delimiter)
    elif 'naughty' in label:
        naughtyfile.write(k)
        naughtyfile.write(delimiter)
    elif 'playful' in label:
        playfulfile.write(k)
        playfulfile.write(delimiter)
    elif 'masti' in label:
        mastifile.write(k)
        mastifile.write(delimiter)
    elif 'item' in label:
        itemfile.write(k)
        itemfile.write(delimiter)
    elif 'rock' in label:
        rockfile.write(k)
        rockfile.write(delimiter)
    elif 'pop' in label:
        popfile.write(k)
        popfile.write(delimiter)
    elif 'motivational' in label:
        motivationalfile.write(k)
        motivationalfile.write(delimiter)
    elif 'remix' in label:
        remixfile.write(k)
        remixfile.write(delimiter)
    elif 'love' in label:
        lovefile.write(k)
        lovefile.write(delimiter)
    elif 'story' in label:
        storyfile.write(k)
        storyfile.write(delimiter)
    elif 'dance' in label:
        dancefile.write(k)
        dancefile.write(delimiter)
