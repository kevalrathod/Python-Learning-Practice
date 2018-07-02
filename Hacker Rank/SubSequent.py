def merge(string, k):
	#Logic of merge
	substring=''
	for i in range(0,len(string),k):
		substring=string[i:i+k]
		print ''.join(sorted(set(substring),key=substring.index))

if __name__ == '__main__':
	string, k = input(), int(input())
	merge(string,k)