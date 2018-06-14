def posneg(input_array):
	left_index=0
	length=len(input_array)
	right_index=length-1
	temp=0
	for i in range(0,length):
		if input_array[left_index]>0:
			temp=input_array[left_index]
			input_array[left_index]=input_array[right_index]
			input_array[right_index]=temp
			right_index=right_index-1
		elif input_array[left_index]<0:
			left_index=left_index+1
	print(input_array)
input_array=[4,-1,9,-1,7,-1,0]
posneg(input_array)
