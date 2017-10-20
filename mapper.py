#!/usr/bin/env python

import sys
from nltk import tokenize
import numpy as np
from textblob import TextBlob

infile=sys.stdin  #taking input from standard input
print (infile)
text = infile.read()
#tokenizing to sentences
ls=tokenize.sent_tokenize(text)

myarray = np.asarray(ls)

subary = []
i=0
while i<len(myarray):
    sen=myarray[i]
    a,b=TextBlob(sen).sentiment ##checking for subjectivity of sentences
    if b > 0:
        subary.append(sen)
    	#print('%s\t%s' % (b, sen))
       # print sen
       # print b
    i=i+1

for val in subary:
    print (val)  #to standard output .the output from this will be further used by reducer.
