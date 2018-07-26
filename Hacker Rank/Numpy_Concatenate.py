import numpy
n,m,p=map(int,input().split())
l1=[]
l2=[]
for i in range(n):
    l1.append(list(map(int,input().split())))
for i in range(m):
    l2.append(list(map(int,input().split())))
a1=numpy.array(l1)
a2=numpy.array(l2)
print(numpy.concatenate((a1,a2),axis=0))