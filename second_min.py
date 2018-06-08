import math
def second_min(input_array):
	min_1=math.inf
	min_2=math.inf

	for i in range(0, len(input_array)):
		if(min_1>input_array[i]):
			min_2=min_1
			min_1=input_array[i]
		elif(min_2>input_array[i]):
			min2=input_array[i]
	print(min_2)
input_array=[4,15,10,51,5,1]
second_min(input_array)