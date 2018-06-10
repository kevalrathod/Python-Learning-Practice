def alternative_array(array1,array2):
	len1=len(array1)
	len2=len(array2)
	total_len=len1+len2
	index1=0
	index2=0
	new_list=[0]*total_len
	for i in range(0,total_len):
		if i%2==0:
			if index1<len1:
				new_list[i]=array1[index1]
				index1=index1+1
			else:
				new_list[i]=array2[index2]
				index2=index2+1
		else:
			if index2<len2:
				new_list[i]=array2[index2]
				index2=index2+1
			else:
				new_list[i]=array1[index1]
				index1=index1+1
	print(new_list)
array1=[1,2,3,10,17]
array2=[5,6,7]
alternative_array(array1,array2)