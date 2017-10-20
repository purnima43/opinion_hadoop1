
#!/usr/bin/env python
import sys

#block3
from nltk.tag import pos_tag


subary = []
for j in sys.stdin: #again from standard input .It is the output of mapper
    subary.append(j)	
 
i=0
t=0
propernouns = dict()
while i<len(subary):
    sentence = subary[i]
    tagged_sent = pos_tag(sentence.split())# splitting sentences
    i = i+1
# [('Michael', 'NNP'), ('Jackson', 'NNP'), ]
    n = len(tagged_sent)
 
    for j in range(1,n):  #features ,modifiers are collected as adjectives adverbs and nouns.
        e,f = tagged_sent[j-2]
        c,d = tagged_sent[j-1]
        a,b = tagged_sent[j]
        if b == 'NN' and  d == 'JJ':
            if f == 'RB':
               #propernouns[j-2] = (e,f)
                propernouns[t]=(e,f)
                #ropernouns.append(e,f)
                t=t+1
                propernouns[t] = (c,d)
                t=t+1
                propernouns[t] = (a,b)
                t=t+1
            else:
                propernouns[t] =  (c,d)
                t=t+1
                propernouns[t]= (a,b)
                t=t+1
#block4        
list1,list2 = [],[]
for i in sorted(propernouns):
    a,b = propernouns[i]
    if b != 'NN':
        list2.append(a)
    else:
        list2.append(a)
        list1.append(list2)
        list2 = []


print('\n'.join(map(str, list1)))# to the output 
