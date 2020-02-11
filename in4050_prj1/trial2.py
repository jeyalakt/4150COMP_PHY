import numpy as np,itertools
arr=np.arange(9).reshape((3,3))

print(arr)
d=0
y=0
#tra=np.random.sample(range(5),5);
#
comb=list(itertools.permutations([1,2,3]))
#comb=list(itertools.permutations(arr))
print(comb)
s=len(comb)
print(s)
dprev=0
set={d:y}
#y=[]
for l in range (len(comb)):

    y=comb[l]
    print(y)
    prev=1
    d=0

    for i in (y):
    #    print(i)
        print()
        val=arr[prev-1][i-1]
        print(val)
        print()
        d=d+val
        prev=i
        print (d)

    if d>=dprev:

        dprev=d
    else:
        print("y", y, d)
        #dprev = dprev
    set[d]=y
    print(set)
    del set[0]
    set.pop(0,0)
    set.items()

    print (min(set.items(),key=lambda k:set[k]))
    """
    d.items()
    [(320, 1), (321, 0), (322, 3)]
    >> >  # find the minimum by comparing the second element of each tuple
    >> > min(d.items(), key=lambda x: x[1])
    (321, 0)
    """