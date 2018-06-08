def pattern(input_num):
    count=1
    #inner loop
    for i in range(0,input_num):
        for j in range(0,i+1):
            print(count,end=" ")
            count+=1
        print("\r")
input_num=4
pattern(input_num)
            
    
