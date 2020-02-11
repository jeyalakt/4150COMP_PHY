import os , numpy as np ,csv, pandas
filename= 'C:/Users/Bruker/in4050/european_cities.csv'
l=np.genfromtxt(f,float,skip_header=1)
print(l)
"""
city_column=[]
file_array=[]
citynames=[]
y=[]
#file_array=np.loadtxt(open(filename),delimiter=';',skiprows=1)
#print(file_array)
#print(np.size(file_array))
with open(filename) as f:
    lines=csv.reader(f,delimiter=';')
    """
    """
    x=list(lines)
    arr=np.array(x).astype("float")
    print(aar)
    """
    """
    citynames=next(lines)
    print(citynames)
    print(len(citynames))

    file=np.loadtxt(f,delimiter=';')
    first_del=np.delete(file,0,axis=0)
    np.savetxt("city.csv",first_del,delimiter=',')
    line = csv.reader('city.csv', delimiter=',')

    x=list(line)
    arr=np.array(x).astype("float")
    print(aar)

    for row in lines:
        #print (row)

        #print()
        for i in range (len(citynames)):

            y=float(row[i])
        print(y)
"""


