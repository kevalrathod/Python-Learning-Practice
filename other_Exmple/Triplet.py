# Three arrays of the same size are given. Find a triplet such that (maximum – minimum) in that triplet is the minimum of all the triplets. A triplet should be selected in a way such that it should have one number from each of the three given arrays. This triplet is the happiest among all the possible triplets. Print the triplet in decreasing order. If there are 2 or more smallest difference triplets, then the one with the smallest sum of its elements should be displayed.

# Input:
# The first line of input contains an integer T denoting the number of test cases. Each test case contains number of elements in array a[], b[] and c[] as n and next  3 lines contain space separated n elements in the arrays a[], b[] and c[] respectively.

# Output:
# Output three space separated integers which form the happiest triplet.

# Constraints:
# 1<=T<=100
# 1<=n<=1000
# 1<= a[i], b[i] ,c[i] <=100000

# Example:
# Input:
# 2
# 3
# 5 2 8
# 10 7 12 
# 9 14 6
# 4
# 15 12 18 9
# 10 17 13 8
# 14 16 11 5
# Output:
# 7 6 5
# 11 10 9


import math
from itertools import groupby
from operator import itemgetter
def tripletCount(l1,l2,l3):
	l5=[]
	l6=[]
	min=math.inf
	l5=l1+l2+l3
	print(sorted(l5))
	data=[1,2,3,4,5,6,12,13,45,32,17]
	for k, g in groupby(enumerate(data) ,lambda (i,x):i-x):
		print(map(itemgetter(1), g))
	# for i in range(0,len(l5)):
	# 	if l5[i+1]-l5[i]==1:
	# 		l6.append(l5[i])
	# print(l6)
	# print("numbers: ",l5[m],l5[n],l5[p])
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=list(map(int,input().split()))
tripletCount(l1,l2,l3)