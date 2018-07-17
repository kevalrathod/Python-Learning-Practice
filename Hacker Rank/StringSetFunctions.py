n1=int(input())
n2=set(map(int, input().split())) 
for i in range(int(input())):
    operation=input().split()
    if(operation[0]=="intersection_update"):
        s1=set(map(int, input().split()))
        n2.intersection_update(s1)
        print(n2)
    elif(operation[0]=="update"):
        s2=set(map(int,input().split()))
        n2.update(s2)
        print(n2)
    elif(operation[0]=="symmetric_difference_update"):
        s3=set(map(int, input().split()))
        n2.symmetric_difference_update(s3)
        print(n2)
    elif(operation[0]=="difference_update"):
        s4=set(map(int,input().split()))
        n2.difference_update(s4)
        print(n2)
print(sum(n2))

        
