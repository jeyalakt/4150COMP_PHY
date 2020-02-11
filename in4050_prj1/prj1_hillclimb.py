import numpy as np,csv,itertools,time
#from numba import jit
from operator import itemgetter
import matplotlib.pyplot as plt

#read csv file and store as 2D
f= 'C:/Users/Bruker/in4050/european_cities.csv'
arr=np.genfromtxt(f,"float",skip_header=1,delimiter=';')
#print(arr)
data=arr.reshape(arr.shape[0],-1)
m,n=np.shape(data)
#print("m,n",m,n)
# required size of subset array
req_subset_size=5
#by inserting 0 row and 0 column to get normal indexes

subdata=np.zeros((req_subset_size+1,req_subset_size+1)) #4   # to create a array of 1 row and column added
for i in range( 1, req_subset_size+1): #4
    for j in range (1,req_subset_size+1):#4
        subdata[i][j]=data[i-1][j-1]
print("subdata of distance ",subdata)
# 5 X 5 city array

starttime=time.time()

#########
citynames=[]
subcity=[]
with open(f) as f:
    lines=csv.reader(f,delimiter=';')
    citynames=next(lines) # to delete header of city names
    #print(citynames)
    print(len(citynames))

    subsetlength=req_subset_size #3  # required array size
    subset=np.arange(1,subsetlength+1)
    print("subset of required size",subset)
    subcity=citynames[0:subsetlength]
    print("cities to travel",subcity)
    #print(subcity)
comb=list(itertools.permutations(subset))
print("all permutations",comb)
s=len(comb)
print("no. of total permutations",s)
############
d=0
tot=0
y=0
dprev=0
set={y:tot}


for l in range (len(comb)):
    y=comb[l]
    #print("permutation ",y) # needed to see results
    len2=len(y)
    #print("length of permutation ",len2)
    prev=0
    tot=0
    for pp in range (0,len2):
        #print("y value",y[pp])
        tot+=subdata[prev][y[pp]]
        #print("distance to be added",subdata[prev][y[pp]])
        prev=y[pp]
        #print("prev",prev)
    tot=tot+subdata[prev][y[0]]
    #print("total distance ", tot) # needed to see results
    set[y] = tot
#print(" total set with permutation ans distance",set)
#print(len(set))
del set[0]
print("set",set)
#print(len(set))
dataarray=list(set.values())
print(dataarray)
datakeys=list(set.keys())
print("keys",datakeys)
#plt.plot(dataarray)
#plt.show()
"""
minval=min(set.items(), key=itemgetter(1))

stoptime=time.time()
executiontime = stoptime- starttime
print(" permutation for minimum distance and distance value",minval)
tuple=minval[0]
#print(tuple)
lt=len(tuple)
#print (lt)
citynames.insert(0,'0')
#print (citynames)
print ()
print("results:")
print(" mminimum distance to be traveled ", minval[1])
print( " cities to be traveled for minimum distance in order :")
for t in range (0,lt):
        #print(tuple[t])
        print(citynames[tuple[t]])
print( "Time taken for exectution",executiontime)
"""

