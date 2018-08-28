#Without Recursion
# def fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(0, n):
#         temp = a
#         a = b
#         b = temp + b
#     return a

# n=int(input())
# for c in range(0, n):
#     print(fibonacci(c))


#using Recursion
def Fibo(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return(Fibo(n-1)+Fibo(n-2))
if __name__ == '__main__':
	n=int(input())
	for i in range(0,n):
		print(Fibo(i))
