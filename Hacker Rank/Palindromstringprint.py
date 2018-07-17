num=int(input())

for i in range(1,num+1):
	for j in range(1, i+1):
		# print('{j}{i-1}'.format(j,i))
		print('{%i} {%j}'.format(i,j))