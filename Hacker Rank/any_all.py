n=int(input())
m=list(map(int,input().split()))
if all(i > 0 for i in m):
    if any(str(i)==str(i)[::-1] for i in m):
        print('True')
    else:
        print('False')
else:
    print('False')