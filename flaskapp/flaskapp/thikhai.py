from __future__ import division
import nltk
import numpy as np
from nltk.book import *
from nltk.tokenize import sent_tokenize, word_tokenize
import math
import random


ex="According to Jain texts, Bahubali was born to Rishabhanatha and Sunanda during the Ikshvaku dynasty in Ayodhya.[2][3][4][5] He is said to have excelled in studying medicine, archery, floriculture, and the knowledge of precious gems. Bahubali had a son named Somakirti (also known as Mahabala).[6] When Rishabhanatha decided to become a monk, he distributed his kingdom among his 100 sons. Bharata was gifted the kingdom of Vinita (Ayodhya) and Bahubali got the kingdom of Asmaka from South India, having Podanapur as its capital.[7] After winning six divisions of earth in all directions (digvijaya), Bharata proceeded to his capital Ayodhyapuri with a huge army and divine chakra-ratna—spinning, disk-like super weapon with serrated edges.[7] But the chakra-ratna stopped on its own at the entrance of Ayodhyapuri, signalling to the emperor that his 99 brothers have yet not submitted to his authority.[8] Bharata's 98 brothers became Jain monks' and submitted their kingdoms to him. Bahubali was endowed with the final and superior body of extraordinary sturdiness and strength (vajra-ṛṣabhanārācasaṃhanana) like Bharata.[9] He hurled open defiance at the chakravartin and challenged him to a fight.[10]The ministers on both sides gave the following argument to prevent war; The brothers themselves, cannot be killed by any means; they are in their last incarnations in transmigration, and possess bodies which no weapon may mortally wound in warfare! Let them fight out the issue by themselves in other ways.[11] It was then decided that to settle the dispute, three kinds of contests between Bharata and Bahubali would be held. These were eye-fight (staring at each other), water-fight (jala-yuddha), and wrestling (malla-yuddha). Bahubali won all the three contests over his elder brother, Bharata."
snt= sent_tokenize(ex)
print(snt)
wrd= word_tokenize(ex)
print(wrd)
fdist1 = FreqDist(wrd)
print(fdist1)
no_of_t=0
no_of_s=0
l=0
s= []
f= []
g= []
m= []
count=0
dis=0
bnt=0
jnt=0
vnt=0
smm=0
tr= []
fic=0
#snt contains each sentences
#s contains score of each sentence
#f is array containing random no of centroids
#g contains clusters
for i in wrd:
    no_of_t = no_of_t +1 ;
print(no_of_t)    
for i in snt:
    no_of_s = no_of_s +1 ;
for j in snt:
    u=word_tokenize(j)
    for k in u:
        tf= fdist1[k]/no_of_t
        idf= math.log(no_of_s/tf)
        l=l+(tf*idf)
        count=count+1 
    s.append(l/count)   
    count=0
    l=0

for h in s:
 print(h)
 

a=3

print(a)


for num in range(0,a):
    f.append(s[num])
    g.append([])

print("rand no")    
print(f)
for qq in range(0,10):
    for w in s:
        for y in f:
            v=w-y
            if bnt==0:
               dis=abs(v)
               bnt=bnt+1
               g[jnt].append(w)
               jnt=jnt+1
            elif abs(v)<dis:
                g[jnt-1].remove(w)
                dis=abs(v)
                g[jnt].append(w)
                jnt=jnt+1
        jnt=0
        bnt=0
    print(g)    
    for uj in range(0,a):
        print(uj)
        if g[uj]!=[]:
           aa=sum(g[uj])
           bb=len(g[uj])
           print(aa)
           print(bb)
           f[uj]=aa/bb
        if qq<9 :
           g[uj]=[]
           

#here in elif if value of score is less than centroid then it is removed from previous cluster and inserted into the new cluster
print(f)
print("cnt")
print("clusters")    
print(g)

for rr in range(a):
    if len(g[rr])>smm:
        smm=len(g[rr])
        m=g[rr]
        
print("sentence indexs")
print(m)    
ws=len(s)
qqq=len(m)
print(ws)
for ee in range(ws):
    print(ee)
    for cc in range(qqq):
        if m[cc]==s[ee]:
           tr.append(ee)
print(tr)
wa=len(tr)

for zz in tr:
    print(snt[zz])
    fic=fic+1
print("\n")
print("original text ")
print(snt)
print("\n")
print("sumerized text")
for zz in tr:
    print(snt[zz])
print("\n")    
print("No of sentences in original passage",ws)
print("Number of Sentences in summary made by our approach",fic)
print("% of size of text in summary by our approach",(fic/ws)*100)
    
