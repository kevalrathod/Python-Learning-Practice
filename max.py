def maximum(input_array):
	#a=[45,12,34,1,23]
	max=-math.inf
	l=len(input_array)
	for i in range(0,l):
		if(max<input_array[i]):
			max=input_array[i]
	print(max)
input_array=[1,2,3,4,5]
maximum(input_array)
		 
	 
