def fact(n):
	f=1
	if n==0:
		return 1
	else:
		for i in range(1,n+1):
			f=f*i
		return f
if __name__ == '__main__':
	n=int(input("Enter any num:"))
	result=fact(n)
	print(result)