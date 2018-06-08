import math
def minimum(input_array):
	#a=[45,12,34,1,23]
	min=math.inf
	l=len(input_array)
	for i in range(0,l):
		if(min>input_array[i]):
			min=input_array[i]
	print(min)
input_array=[1,2,3,4,5]
minimum(input_array)
		 
	 
