n=int(input())

for i in range(0,n):
    i1=int(input())
    n1=set(map(int,input().split()))
    i2=int(input())
    n2=set(map(int,input().split()))
    n3=n1.union(n2)
    if(n3==n2):
        print('True')
    else:
        print('False')