#!/bin/python3

from operator import itemgetter



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for i in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    k = int(input())
    
    for item in sorted(arr,key=itemgetter(k)):
        print(*item)