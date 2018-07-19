import math
cube = lambda x: pow(x,3)
def fibonacci(n):
    #FIRST METHOD
    # lis = [0,1]
    # for i in range(2,n):
    #     lis.append(lis[i-2] + lis[i-1])
    # return(lis)

    #SECOND METHOD
    l=[]
    for i in range(0,n):
        l.append(i if i < 2 else l[i-2]+l[i-1])
    return(l)



if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))