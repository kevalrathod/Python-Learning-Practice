def indexRange(l):
	n=int(input("Enter num :"))
	for i in range(0,len(l)):
		if l[i]==n:
			print("The index of give n in l is ",i)

	
l=[1,2,3,4,5]
indexRange(l)