def Insertion(input_array):
	lenght=len(input_array)
	for i in range(1, lenght-1):
		tmp=input_array[i]
		index=i
		while index>0 and input_array[index-1] > tmp:
			input_array[index] =input_array[index-1]
			index=index-1
		input_array[index]=tmp
	print(input_array)
input_array=[3,1,4,2,6]
Insertion(input_array)
