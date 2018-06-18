import math
if __name__ == '__main__':
	n=int(input())
	scorelist=[]
	final=[]
	minimum1=math.inf
	minimum2=math.inf
	i=0
	for i in range(0,n):
		name = input()
		score= float(input())
		scorelist.append([name,score])
	print(scorelist)
	for i in range(0,len(scorelist)):
		if minimum1>scorelist[i][1]:
			minimum2=minimum1
			minimum1=scorelist[i][1]
		elif minimum1<scorelist[i][1] and minimum2>scorelist[i][1]:
			minimum2=scorelist[i][1]
	print(minimum2)
	for i in range(0,len(scorelist)):
		if scorelist[i][1]==minimum2:
			final.append(scorelist[i][0])
	for i in sorted(final):
		print(i)