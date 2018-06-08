def pattern(number):
    count=1
    #inner loop
    for i in range(0,number):
        for j in range(0,number):
            print(num,end=" ")
            count=count+1
        print("\r")
number=4
pattern(number)
