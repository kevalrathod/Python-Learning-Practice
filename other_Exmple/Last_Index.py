def enterNum(num):
	count=0
	for i in num:
		if i=='0':
			count=count+1
		else:
			print(count)
	print(num)
num=input("Enter Any Number")
enterNum(num)