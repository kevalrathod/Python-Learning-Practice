import math
def min(input_list):
	min1=math.inf
	for i in range(0,len(input_list)):
		if(input_list[i]<min1):
			min1=input_list[i]
	print(min1)

input_list=list(map(int,input().split()))
min(input_list)