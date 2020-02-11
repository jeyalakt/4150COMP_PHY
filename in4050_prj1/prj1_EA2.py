import numpy as np,csv,itertools,time, random
#from numba import jit
from operator import itemgetter

outf = open('op.txt', 'w+')
outf.write("EA algorithms \n")
outf.write("\n")
outf.close()

def main():
    #np.random.seed(10)
    # read csv file and store as 2D
    f = 'C:/Users/Bruker/in4050/european_cities.csv'
    arr = np.genfromtxt(f, "float", skip_header=1, delimiter=';')
    # print(arr)
    data = arr.reshape(arr.shape[0], -1)
    m, n = np.shape(data)
    # print("m,n",m,n)
    # required size of subset array
    # req_subset_size=7

    #by inserting 0 row and 0 column to get normal indexes
    emptyarr=[]
    subdata=np.zeros((req_subset_size+1,req_subset_size+1)) #4   # to create a array of 1 row and column added
    for i in range( 1, req_subset_size+1): #4
        for j in range (1,req_subset_size+1):#4
            subdata[i][j]=data[i-1][j-1]
    print("subdata of distance ",subdata)
    # 5 X 5 city array

    starttime=time.time()

    #########
    citynames=[]
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

    def EA(p1,p2,index_start,index_stop,order_startindex,order_stopindex):

        p1=list(p1)
        p2=list(p2)
        print("p1 first",p1)
        print("p2 first",p2)
        l1_p1=len(p1)

        ##########
        # inversion mutation
        #########
        #index_start=2
        #index_stop=l1_p1-2

        p1_sub=p1[index_start:index_stop]
        p2_sub=p2[index_start:index_stop]
        #for i in range (index_start,index_finish):
        #print(p1_sub)
        #print(p2_sub)
        p1_sub=p1_sub[::-1]
        p2_sub=p2_sub[::-1]
        #print(p1_sub)
        #print(p2_sub)
        p1[index_start:index_stop]=p1_sub
        p2[index_start:index_stop]=p2_sub
        print("p1 after inverse mutation",p1)
        print("p2 after inverse mutation",p2)
        ############

        # order crossover
        ###############
        c1=[0]*len(p1)
        #c2=[0]*len(p2)
        #order_startindex=2
        #order_stopindex=order_startindex+2
        #print("stopindex",order_stopindex)
        c1[order_startindex:order_stopindex]=p1[order_startindex:order_stopindex]
        #print("c1",c1)
        #c2[order_startindex:order_stopindex]=p2[order_startindex:order_stopindex]
        #print("c2",c2)
        for i in range ( order_stopindex,len(c1)):
            emptyarr.append(i)
        #print (emptyarr)
        for i in range (0,order_startindex):
            emptyarr.append(i)
        #print (emptyarr)

        for i in range (order_stopindex,len(p1)):
            search=p2[i]
            #print(search)
            if search not in c1:
                c1[emptyarr[0]] = search
                del emptyarr[0]

        for i in range (0, order_startindex):
            search = p2[i]
            #print(search)
            if search not in c1:
                c1[emptyarr[0]] = search
                del emptyarr[0]

        for i in range (order_startindex, order_stopindex):
            search = p2[i]
            #print(search)
            if search not in c1:
                c1[emptyarr[0]] = search
                del emptyarr[0]
        #print("c1- first child",c1)


        #####
        ## to get city names and distnace
        #####
        tot=0
        y=0
        dprev=0
        dictofperval={y:tot}
        y=c1
        #print("y",y)
        #print("set",dictofperval)
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

        dictofperval[tuple(y)] = tot
        #print(" total set with permutation ans distance",dictofperval)
        #print(len(set))
        del dictofperval[0]
        #print(dictofperval)
        #print(len(set))
        minval=min(dictofperval.items(), key=itemgetter(1))

        #print(" permutation for minimum distance and distance value",minval)
        tupl=minval[0]
        #print(tupl)
        lt=len(tupl)
        #print (lt)
        citynames.insert(0,'0')
        #print (citynames)
        print ()
        #print("results:")
        #print(" mminimum distance to be traveled ", minval[1])
        #print( " cities to be traveled for minimum distance in order :")
        for t in range (0,lt):
                #print(tuple[t])
                hello="idle"
                #print(citynames[tupl[t]])

        del citynames[0]
        #print(tot,tupl)
        return tot,tupl
    numberofiterations=20
    finalleastval=np.zeros(numberofiterations)
    finalleastcit=list()

    for i in range (0, numberofiterations):

        print("iteration", i)
       # """
        l1_p1 = len(p1)
        if req_subset_size <=7:
            index_start = int((random.randrange(req_subset_size)) / 2)
            print("indexstart", index_start)
            index_stop = l1_p1 - 3
            order_startindex = int((random.randrange(req_subset_size)) / 2)
            print("order start", order_startindex)
            order_stopindex = l1_p1 - 2
        elif req_subset_size>7 and req_subset_size<=10:
            index_start = int((random.randrange(req_subset_size)) / 2)
            print("indexstart", index_start)
            index_stop = l1_p1 - 5
            order_startindex = int((random.randrange(req_subset_size)) / 3)
            print("order start", order_startindex)
            order_stopindex = l1_p1 - 3
        else:
            index_start = int((random.randrange(req_subset_size)) / 2)
            print("indexstart", index_start)
            index_stop = l1_p1 - 5
            order_startindex = int((random.randrange(req_subset_size)) / 4)
            print("order start", order_startindex)
            order_stopindex = l1_p1 - 4


        #"""
        c1value, c1cities=EA(p1,p2,index_start,index_stop,order_startindex,order_stopindex)
        print("calc second child")
        c2value, c2cities=EA(p2,p1,index_start,index_stop,order_startindex,order_stopindex)
        print("c1", c1value,c1cities)
        print("c2", c2value,c2cities)
        if (c1value<=c2value):
            #print("least")
            leastval=c1value
            leastcit=c1cities
            #print("c1",c1value,c1cities)
            ########
        else:
            #print("least")
            leastval = c2value
            leastcit = c2cities
            #print("c2", c2value,c2cities)

        #print("c1",c1value)
        #print("c2",c2value)
        print("minimum of 2 children",leastval,leastcit)
        p1=c1cities
        p2=c2cities

        finalleastval[i]=leastval
        finalleastcit.append(leastcit)
        print()
    print("final",finalleastval,finalleastcit)
    print("final all distances",finalleastval)

    arrtolist=finalleastval.tolist()
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
    tupl=finalleastcit[leastindex]
    print("cities for least dist",tupl)
    #print(tupl)
    lt=len(tupl)
    #print (lt)
    citynames.insert(0,'0')
    #print (citynames)
    print ()
    print("results:")
    #print(" mminimum distance to be traveled ", minval[1])
    print( " cities to be traveled for minimum distance in order :")
    for t in range (0,lt):
            #print(tupl[t])
            print(citynames[tupl[t]])
    stoptime=time.time()
    executiontime = stoptime- starttime
    print("Time taken for exectution",executiontime)
    outf = open('op.txt', 'a')
    #header='minimum distances\n'
    #np.savetxt('op.txt',np.array(finalleastval), header=header, fmt='%.3f',newline='\n',comments='')
    outf.write("no.of cities\n")
    outf.write("\n")
    outf.write(str(req_subset_size))
    outf.write("\n")
    outf.write("number of generations\n")
    outf.write("\n")
    outf.write(str(numberofiterations))
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
    outf.write( "{:.3f}".format(meanval))
    outf.write("\n")
    outf.write("std.dev\n")
    outf.write( "{:.3f}".format(sd))
    outf.write("\n")
    outf.write("\n")
    outf.close()
allsub=[7, 8, 10]
for i in range (len(allsub)):
    if __name__ == "__main__":
        req_subset_size= allsub[i]
        print("subset",req_subset_size)
        main()
