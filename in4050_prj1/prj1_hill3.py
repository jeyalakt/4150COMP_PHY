import numpy as np,csv,itertools,time
import random
#from numba import jit
from operator import itemgetter
import matplotlib.pyplot as plt


outf = open('ophillclimb.txt', 'w+')
outf.write("hillclimb algorithms \n")
outf.write("\n")
outf.close()

req_subset_size=5

# read csv file and store as 2D
f = 'C:/Users/Bruker/in4050/european_cities.csv'
arr = np.genfromtxt(f, "float", skip_header=1, delimiter=';')
# print(arr)
data = arr.reshape(arr.shape[0], -1)
m, n = np.shape(data)
# print("m,n",m,n)

# required size of subset array

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
l=list(map(lambda el:[el], comb))
print("l",l[0])
#y=random.choice(l)
#print("y",y)
y=list(l[0][0])
#z=list(l[1])
#print("z",z)
#print("arr",arr)         # prints full array
s=len(comb)
print("no. of total permutations",s)
totarr=[]
cityarr=[]
#cityarr.append(y)
#cityarr.append(z)
#print("first y",cityarr)
############
#y=0
tot=0
#set={y:tot}
#y=comb[0]
#print("y",y)
#set = {y: tot}
#print("set", set)
temp=[]
def hill(y):
    tot = 0
   # set[y]=tot
    d=0
    dprev=0
    prev=0
    len2=len(y)
    for pp in range (0,len2):
        #print("y value",y[pp])
        tot+=subdata[prev][y[pp]]
        #print("distance to be added",subdata[prev][y[pp]])
        prev=y[pp]
        #print("prev",prev)
    tot=tot+subdata[prev][y[0]]
    #print("total distance ", tot) # needed to see results
    totarr.append(tot)
    #print(" total set with permutation ans distance",set)
    #print(len(set))
    #del set[0]
    print("totarr",totarr)
    #print(len(set))
    #dataarray=list(set.values())
    #print(dataarray)
    #datakeys=list(set.keys())
    #print("keys",datakeys)
    #lis=list(datakeys[0])
    lis=y
    temp=list(y)
    cityarr.append(temp)
    print("lis",lis)
    print("cityarr",cityarr)
    return lis

def swapPos(lis, pos1, pos2):
    lis[pos1], lis[pos2] = lis[pos2], lis[pos1]
    return lis
"""
numberofiterations = 20
finalleastval = np.zeros(numberofiterations)
finalleastcit = list()

for i in range(0, numberofiterations):
    print("iteration", i)
"""
result=hill(y)
print()
print("result",result)
print()

for i in range ( 0 ,len(y)-1):
    swapped=swapPos(result,0,i+1)
    print ("swapped lis",swapped)

    #y=0
    #tot=0.0
    #set={y:tot}
    temp=swapped
    #print("set", set)

    y=swapped
    print("y",y)
    #tot=0
    #set = {y: tot}
    #print("set", set)
    result2=hill(y)
    print()
    print("result2",result2)
    #cityarr.append(temp)
    #print("cityarr", cityarr)
    """
    finalleastval[i] = leastval
    finalleastcit.append(leastcit)
    print()
    
    print("final", finalleastval, finalleastcit)
    print("final all distances", finalleastval)
    """

######
minvalfinal=min(totarr)
print("minvalfin",minvalfinal)
indexminvalfinal=totarr.index(minvalfinal)
citylistminfinal=cityarr[indexminvalfinal]
print("citlistfinal",citylistminfinal)
finalleastval=totarr
#arrtolist=finalleastval.tolist()

arrtolist=totarr
#arrtolist=finalleastcit
leastvalofall=min(arrtolist)
print("final- least of all ",leastvalofall)
worstofll=max(arrtolist)
print("final-worst of all",worstofll)
meanval=np.mean(arrtolist)
print("mean", meanval)
sd=np.std(arrtolist)
print("std.dev",sd)
leastindex=arrtolist.index(leastvalofall)
print("least index",leastindex)

#print(" permutation for minimum distance and distance value",minval)
#tupl=finalleastcit[leastindex]
#print("cities for least dist",tupl)


"""
    
    
    
    
    
    for l in range (len(y)):
        #y=comb[l]
        #print("permutation ",y) # needed to see results
        #len2=len(y)
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

outf = open('ophillcimb.txt', 'a')
# header='minimum distances\n'
# np.savetxt('op.txt',np.array(finalleastval), header=header, fmt='%.3f',newline='\n',comments='')
outf.write("no.of cities\n")
outf.write("\n")
outf.write(str(req_subset_size))
outf.write("\n")
#outf.write("number of generations\n")
outf.write("\n")
#outf.write(str(numberofiterations))
outf.write("\n")
outf.write("minimum distances\n")
for line in finalleastval:
    outf.write("{:.3f}".format(line))
    outf.write("\n")
outf.write("best val- i.e shortest dist \n")
outf.write("{:.3f}".format(leastvalofall))
outf.write("\n")
outf.write("worst val- i.e longest dist \n")
outf.write("{:.3f}".format(worstofll))
outf.write("\n")
outf.write("mean\n")
outf.write("{:.3f}".format(meanval))
outf.write("\n")
outf.write("std.dev\n")
outf.write("{:.3f}".format(sd))
outf.write("\n")
outf.write("\n")
outf.close()

