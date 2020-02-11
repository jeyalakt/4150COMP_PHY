import numpy as np,csv,itertools,time, random
#from numba import jit
from operator import itemgetter
np.random.seed(10)

#read csv file and store as 2D
f= 'C:/Users/Bruker/in4050/european_cities.csv'
arr=np.genfromtxt(f,"float",skip_header=1,delimiter=';')
#print(arr)
data=arr.reshape(arr.shape[0],-1)
m,n=np.shape(data)
#print("m,n",m,n)
# required size of subset array
req_subset_size=6
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
p1=random.choice(comb)
p2=random.choice(comb)
p1=list(p1)
p2=list(p2)
print("p1",p1)
print("p2",p2)
l1_p1=len(p1)
l2_p2=len(p2)

# inversion mutation
####
index_start=0
index_stop=l1_p1-2

p1_sub=p1[index_start:index_stop]
p2_sub=p2[index_start:index_stop]
#for i in range (index_start,index_finish):
print(p1_sub)
print(p2_sub)
p1_sub=p1_sub[::-1]
p2_sub=p2_sub[::-1]
print(p1_sub)
print(p2_sub)
p1[index_start:index_stop]=p1_sub
p2[index_start:index_stop]=p2_sub
print(p1)
print(p2)
############

# order crossover
c1=[0]*len(p1)

order_startindex=2
order_stopindex=l1_p1-1
print("stopindex",order_stopindex)
c1[order_startindex:order_stopindex]=p1[order_startindex:order_stopindex]
print("c1",c1)
emptyarr=[]
searcharr=[]

print(order_stopindex)
search=p2[order_stopindex]
print("search",search)
#searchval(search)
#def searchval(search):
for i in range (order_stopindex,len(p1)):
    if search in c1:
        print("yes")
        empty = p2.index(search)
        #print("empty", empty)
        emptyarr.append(empty)
        #print("emptyarr", emptyarr)
    else:
        c1[i]=search
print("c1",c1)
print("emptyarr", emptyarr)

emptyarr2=[]
for i in range (0,order_startindex):
#for i in range(0, len(p2)):
    print("second loop")
    search = p2[i]
    print("search", search)
    if search not in c1:
        if len(emptyarr)==0:
            c1[i] = p2[i]
        else:
            c1[emptyarr[0]] = p2[i]
    else:
        print ("yes")
        empty=p2.index(search)
        #print("empty",empty)
        emptyarr.append(empty)
        print("emptyarr",emptyarr)
        searcharr.append((search))
        print("searcharr",searcharr)
    #else:
        #c1[emptyarr[0]]=p2[i]
#search =p2[i]
print ("c1",c1)
print("emptyarr",emptyarr)
if search in searcharr and c1:
    print ("present")
else:
    print("i not present",search)
print("emptyarr",emptyarr)


for i in range (order_startindex,order_stopindex):
#for i in range(0, len(p2)):
    print("third loop")
    search = p2[i]
    print("search", search)
    if search not in c1:
        if len(emptyarr) == 0:
            c1[i] = p2[i]
        else:
            c1[emptyarr[0]] = p2[i]
    else:
        print("yes")
        empty = p2.index(search)
        # print("empty",empty)
        emptyarr.append(empty)
        print("emptyarr", emptyarr)
        searcharr.append((search))
        print("searcharr", searcharr)
    # else:
    # c1[emptyarr[0]]=p2[i]
    # search =p2[i]
print("c1", c1)
print("emptyarr", emptyarr)
if search in searcharr and c1:
    print("present")
else:
    print("i not present", search)
print("emptyarr", emptyarr)

"""
"""
#########################

"""
d=0
tot=0
y=0
dprev=0
set={y:tot}
"""
"""
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
print(" total set with permutation ans distance",set)
#print(len(set))
del set[0]
print(set)
#print(len(set))

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
