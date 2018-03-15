from __future__ import unicode_literals
from hazm import *
import re

regex = re.compile(' *\w+ *')
englishLetter = re.compile('[a-zA-Z0-9]')
normalizer = Normalizer()

lines = tuple(open('100.txt', 'r'))
valuable = open('valuable.txt', 'w')
outOfVocab = open('outOfVocabulary.txt', 'w')
all = open('all.txt', 'w')

dict = {}

for idx,line in enumerate(lines):
    print(idx)
    lineStr = ' '.join(regex.findall(line))
    lineStr = normalizer.normalize(lineStr)
    tokenizedList = word_tokenize(lineStr)
    #all.write(' '.join(tokenizedList)+' ')
    for i in tokenizedList:
        if(englishLetter.search(i)):
            continue
        if(i in dict):
            dict[i] += 1
        else:
            dict[i] = 1

        all.write(i+' ')

for key in dict:
    if(dict[key] >= 5):
        valuable.write(key+' ')
    else:
        outOfVocab.write(key+' ')
