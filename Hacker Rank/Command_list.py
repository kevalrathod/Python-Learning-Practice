if __name__ == '__main__':
    N = int(input())
    list1=[]
    for i in range(0,N):
    	input_string=input()
    	if(input_string.startswith("insert")):
    		str, i,e =input_string.split(" ")
    		list1.insert(int(i),int(e))
    	elif(input_string.startswith("print")):
    		print(list1)
    	elif(input_string.startswith("append")):
    		a_string,num = input_string.split(" ")
    		list1.append(int(num))
    	elif(input_string.startswith("remove")):
    		r_string,e = input_string.split(" ")
    		list1.remove(int(e))
    	elif(input_string.startswith("sort")):
    		list1.sort()
    	elif(input_string.startswith("pop")):
    		list1.pop()
    	elif(input_string.startswith("reverse")):
    		list1.reverse()


