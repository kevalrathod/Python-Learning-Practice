def merge_arry(array1,array2):
	len1=len(array1)
	len2=len(array2)
	total_len=len1+len2

	merged_list=[0]*total_len
	for i in range(0,total_len):
		if i < len(array1):
			merged_list[i]=array1[i]
		else:
			merged_list[i]=array2[i-len(array1)]
	print(merged_list)
#print(array1)
array1=[4,5,6]
array2=[7,8,9,12,14]
merge_arry(array1,array2)