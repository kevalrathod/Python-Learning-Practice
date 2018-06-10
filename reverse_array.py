def reverse_array(input_array):
	size=len(input_array)
	loop_val = size//2
	index=size-1
	for i in range(0,loop_val):
		temp=input_array[index]
		input_array[index]= input_array[i]
		input_array[i]=temp
		index=index-1
	print(input_array)
	print("Got the reverse_array")
input_array=[1,2,3]
reverse_array(input_array)

