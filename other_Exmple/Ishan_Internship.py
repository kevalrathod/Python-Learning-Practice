# Ishaan wants to intern at GeeksForGeeks but for that he has to go through a test. There are N candidates applying for the internship including Ishaan and only one is to be selected.
# Since he wants to qualify he asks you to help him. The test is as follows.
# The candidates are asked to stand in a line at positions 1 to N and given a number K. Now, every Kth candidate remains and the rest are eliminated. This is repeated until the number of candidates are less than K.
# Out of the remaining candidates, the one standing at smallest position is selected. You need to tell Ishaan at position he must stand to get selected.

# Input : 
# First line of input contains a single integer T denoting the number of test cases.
# The only line of each test case contains 2 space-separated integers N denoting number of candidates and  K.

# Output : 
# For each test case, print the required position in a new line.

# Constraints : 
# 1 <= T <= 100
# 1 <= N <= 10^5
# 2 <= K <= 10

# Example : 
# Input : 
# 3
# 30 3
# 18 3
# 5 2
# Output : 
# 27
# 9
# 4




def Recursive(input_list,k):
	print('Input_list = ',input_list)
	if len(input_list)==k:
		print(input_list[-1])
		return
	elif len(input_list)<k:
		print(input_list[0])
		return
	output_list=[]
	for i in range(0,len(input_list)):
		if (i+1)%k==0:
			output_list.append(input_list[i])
	Recursive(output_list,k)
if __name__ == '__main__':
	n=int(input("Enter candidate: "))
	k=int(input("Enter Kth value: "))
	input_list=[]
	for i in range(1,n+1):
		input_list.append(i)
	Recursive(input_list,k)