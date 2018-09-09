# An array containing positive elements is given. ‘A’ and ‘B’ are two numbers defining a range. Write a function to check if the array contains all elements in the given range.

# Input:
# The first line of input contains an integer T denoting the number of test cases. Each test case contains space separated integers n, A and B which denotes the number of elements in the array a[] and the range [A, B]. Next line contains space separated n elements in the array a[].

# Output:
# Print "Yes" if all the elements in the range are present else print "No"+




def Sets(s1,s2):
	if(s2==s1.union(s2)):
		return True
	else:
		return False

if __name__ == '__main__':
	s1=set(map(int,input().split()))
	s2=set(map(int,input().split()))
	result=Sets(s1,s2)
	print(result)