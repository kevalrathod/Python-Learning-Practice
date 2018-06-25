def swap_case(s):
    count1=0
    count2=0
    count3=0
    newstring=''
    i=0
    for i in s:
        if(i.isupper())==True:
            count1+=1
            newstring+=(i.lower())
        elif(i.islower())==True:
            count2+=count1
            newstring+=(i.upper())
        
             count3+=1
             newstring+=i
    return newstring


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

