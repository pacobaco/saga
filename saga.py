import numpy as np
import math
o = open('c:\\saga\\fullcorpstats.csv')
o = o.read()
o = o.split('\n')

s = {}

def cosine_similarity(a, b):
    return sum([float(i)*float(j) for i,j in zip(a, b)])/(math.sqrt(sum([float(i)*float(i) for i in a]))* math.sqrt(sum([float(i)*float(i) for i in b]))) 

for x in o:
    y = x.split(',')
    try:
        s[y[0]]=[y[1],y[2],y[3],y[5],y[6]]
    except: continue

q = {}

for x in list(s.keys()):
        q[x]={}
        for y in list(s.keys()):
            try:
                q[x][y]=cosine_similarity(s[x],s[y])
            except: continue
