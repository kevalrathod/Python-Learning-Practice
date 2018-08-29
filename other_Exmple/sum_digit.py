# Given a positive value N, we need to find the count of numbers smaller than and equal to N such that the difference between the number and sum of its digits is greater than or equal to given specific value k.

# Input:
# The first line of input contains an integer T denoting the number of test cases. Each test case contains two space separated integers N and k.

# Output:
# Print an integer which is the required value.

# Constraints:
# 1<=T<=50
# 1<=N,k<=109


def  sum_Digit(n,m):
	sum=0
	if n<10 and m==0:
		print("count is :",n)
	elif n>=10 and m==0:
		print("count is : ", n)
	elif n>=10 and m>9:
		print("No number Sorry..!")
	elif n>=10 and m<=9:
		while n>0:
			dig=n%10
			sum=sum+dig
			n=n//10
		print("Count is: ", sum)
if __name__ == '__main__':
	n,m= map(int,input().split())
	sum_Digit(n,m)