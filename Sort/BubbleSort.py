def bubbleSort(input_array):
	length = len(input_array)
	for i in range(length):
		for j in range(0, length-i-1):
			if input_array[j] > input_array[j+1]:
				input_array[j], input_array[j+1] = input_array[j+1], input_array[j]
	print(input_array)
input_array = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(input_array)
