from collections import Counter

def Count_Total(n,l,c):
	income=0
	for i in range(0,c):
		size,price=map(int,input().split())
		if numer_list[size]:
			print(numer_list[size])
			numer_list[size]=numer_list[size]-1
			# income=income+price
			# numer_list[size]-=1
	# print(income)

if __name__ == '__main__':
    n_shoe=int(input())
    numer_list=Counter(map(int, input().split()))
    cust=int(input())

    Count_Total(n_shoe,numer_list,cust)
