n,m=input().split()
Z= input().split()
A=input().split()
B=input().split()

for i in Z:
	if i in A:
		happnes+=1
	if i in B:
		happnes-=1
print(happnes)