a= int(input())
for i in range(0,a):
    try:
    	b,c= map(int,input().split())
        ans=b//c
        print(ans)
    except(ValueError,ZeroDivisionError) as e:
        print(" Error code :", e)
