def palindrom(string):
	length=len(string)
	for i in range(0,length//2):
		if string[i]!=string[length-i-1]:
			return False
	return True
string="wowow"
if palindrom(string):
	print("yes, input string is palindrom")
else:
	print("No,Input string is not palindrom")

