def count_substring(string,sub_string):
	count=0
	for i in range(0, len(string)):
		if string[i:i+len(sub_string)]==sub_string:
			//print("count increase", i)
			count=count+1
		else:
			//print("count not increase",i)
	return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)