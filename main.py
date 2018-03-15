from __future__ import unicode_literals
from hazm import *
import re

regex = re.compile(' *\w+ *')

lines = tuple(open('100.txt', 'r'))
valuable = open('valuable.txt', 'w')
outOfVocab = open('outOfVocabulary.txt', 'w')
all = open('all.txt', 'w')

dict = {}

for idx,line in enumerate(lines):
    print(idx)
    tmp = word_tokenize(' '.join(regex.findall(line)))
    all.write(' '.join(tmp)+' ')
    for i in tmp:
        if(i in dict):
            dict[i] += 1
        else:
            dict[i] = 1

for key in dict:
    if(dict[key] >= 5):
        valuable.write(key+' ')
    else:
        outOfVocab.write(key+' ')
