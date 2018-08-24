def sumFromTwoArrays(list1,list2,x):
    left = 0
    right = len(list2)-1
    #print(left,right)
    diff=99999
    while(left<len(list1) and right >=0):
        if(list1[left]+list2[right]-x < diff):
            res1 = list1[left]
            res2 = list2[right]
            diff = list1[left]+list2[right]-x
        if(list1[left]+list2[right]>x):
            right = right-1
        else:
            left = left+1
    print (res1,res2)

list1 = [9,10,20,30,40]
list2 = [11,12,13,14,15]
x = 24
sumFromTwoArrays(list1,list2,x)