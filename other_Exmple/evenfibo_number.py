def evenFib(n) :
    if (n < 1) :
        return n
    if (n == 1)  :
        return 2
  
    # recursion
    return ((4 * evenFib(n-1)) + evenFib(n-2)) 

if __name__ == '__main__':
	n=int(input())
	result=evenFib(n)
	print(result)