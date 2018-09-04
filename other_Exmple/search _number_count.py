# Given an sorted array of size n. Find number of elements which are less than or equal to given element.
# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
# Each test case contains an integer n denoting the size of the array. Then the next line contains n space separated integers forming the array.
# Output:
# Print the number of elements which are less than or equal to given element.


def search(n,nums,target):
        first = 0
        last = n-1
        middle = int((first+last)/2)
        while first<= last:
            if nums[middle] <= target:
                first = middle + 1
            else:
                last = middle - 1
            middle = int((first+last)/2)
            if first > last:
                return first
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    target = int(input())
    result=search(n,arr,target)
    print(result)