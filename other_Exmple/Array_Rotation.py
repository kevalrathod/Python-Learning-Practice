N=3
def Rotation(arry):	
	tmp=0
	for i in range(0,int(N/2)):
		for j in range(0,N-i-1):
			tmp=arry[i][j]
			arry[i][j]=arry[j][N-i-1]
			arry[j][N-i-1]=arry[N-i-1][N-j-1]
			arry[N-i-1][N-j-1]=arry[N-j-1][i]
			arry[N-j-1][i]=tmp
def Display(arry):
	for i in range(0,N):
		for j in range(0,N):
			print(arry[i][j],end=' ')
		print(" ")

arry=[[1,2,3],[4,5,6],[7,8,9]]
Rotation(arry)
Display(arry)