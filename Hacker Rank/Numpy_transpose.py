import numpy
n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
a=numpy.array(l)
print(numpy.transpose(a))
print(a.flatten())