import os , numpy as np ,csv, pandas, itertools
from operator import itemgetter
from itertools import groupby
from operator import itemgetter
f= 'C:/Users/Bruker/in4050/european_cities.csv'
arr=np.genfromtxt(f,"float",skip_header=1,delimiter=';')

print(arr)
data=arr.reshape(arr.shape[0],-1)
subdata=np.zeros((6,6)) #4
for i in range( 1, 6): #4
    for j in range (1,6):#4
        subdata[i][j]=data[i-1][j-1]
print("subdata",subdata)
m,n=np.shape(data)
print("m,n",m,n)

#########
citynames=[]
namelist=[]
subcity=[]
with open(f) as f:
    lines=csv.reader(f,delimiter=';')
    citynames=next(lines)
    print(citynames)
    print(len(citynames))


    subsetlength=5 #3
    subset=np.arange(1,subsetlength+1)
    print(subset)
    subcity=citynames[0:subsetlength]
    print(subcity)
    #print(subcity)
comb=list(itertools.permutations(subset))
print(comb)
s=len(comb)
print(s)
############
d=0
tot=0
y=0
dprev=0
set={y:tot}
for l in range (len(comb)):
    y=comb[l]
    print("y",y)
    len2=len(y)
    print("len2",len2)
    prev=0
    tot=0
    for pp in range (0,len2):
        print("y values",y[pp])
        tot+=subdata[prev][y[pp]]
        print("dta",subdata[prev][y[pp]])
        prev=y[pp]
        print("prev",prev)
    tot=tot+subdata[prev][y[0]]
    print("total", tot)
    set[y] = tot
print(set)
print(len(set))
    #del pop[0]
del set[0]
print(set)
print(len(set))

minval=min(set.items(), key=itemgetter(1))
print(minval)
tuple=minval[0]
print(tuple)
lt=len(tuple)
print (lt)
citynames.insert(0,'0')
print (citynames)

for t in range (0,lt):
        print(tuple[t])
        print(citynames[tuple[t]])


"""
for i in range (0,length):

    namelist[i]=citynames[i]
"""
print (citynames.index('Berlin'))
#print (namelist)

