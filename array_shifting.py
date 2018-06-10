def array_shift(input_arry):
	size=len(input_arry)
	# range_shift=size//2
	no_of_shift=2
	index=size-1
	
	for i in range(0,no_of_shift):
		temp=input_arry[0]
		for j in range(0,index):			
			# input_arry[index]=temp
			input_arry[j]=input_arry[j+1]			
		input_arry[index]=temp
	print(input_arry)
	# print(temp)
input_arry=[1,2,3,4,5]
array_shift(input_arry)

