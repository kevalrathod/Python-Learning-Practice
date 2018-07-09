A=int(input())
a=set(map(int,input().split()))
B=int(input())
b=set(map(int,input().split()))

p=a.difference(b)
q=b.difference(a)
z=p.union(q)

print('\n'.join(sorted(z,key=int)))