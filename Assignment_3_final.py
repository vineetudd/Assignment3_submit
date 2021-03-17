##ASSIGNMENT 3
#myreduce function
def myreduce(f,l,initializer=None):
    c=len(l)
    global s
    if initializer is None:
        s=0
        for i in range(c-1):
            if i==0:
                s=f(l[0],l[1])
            else:
                s=f(s,l[i+1])
    else:
        s=initializer
        for i in range(c):
            s=f(s,l[i])
    return s
#myfilter function
def myfilter(f,l):
    c=len(l)
    global s
    for i in range(c):
        if f(l[i])==True:
            yield l[i]
#List Comprehensions
#1.
a=['x','y','z']
[i*j for i in a for j in range(1,5)]
#2.
a=['x','y','z']
[i*j for j in range(1,5)for i in a]
#3.
[[j] for i in range(2,5)for j in range(i,i+3)]
#4.
[[i for i in range(j,j+4)]for j in range(2,6)]
#5.
[(i,j)for j in range(1,4) for i in range(1,4)]

        
