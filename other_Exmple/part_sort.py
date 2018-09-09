def part_Sort(l,n,m):
    for i in range(n, m+1):
        insert_num = l[i]
        for j in range(m, n, -1):
            if l[j-1] <= insert_num:
                l[j] = insert_num
                break
            l[j] = l[j-1]
        else:
			l[0] = insert_num
    return l

if __name__ == '__main__':
	l=list(map(int, input().split()))
	n=int(input())
	m=int(input())
	result=part_Sort(l,n,m)
	print(result)