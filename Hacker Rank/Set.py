def average(array):
    # your code goes here
    # a= map(int, input())
    # a_set=set(a)
    sum=0
    print(array,end="\n")
    a_set=set(array)
    print(a_set,end="\n")
    for x in range(0,len(a_set)):
        sum = sum + list(a_set)[x]
    avg=sum/len(a_set)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)