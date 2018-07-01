# This  code is not correct.!

#under process

def minion_game(string):
	#your code oes here
	vowel=['a','e','i','o','u','A','E','I','O','U']
	count=0;
	substring=string[0:1]
	count_kevin=0
	count_stuart=0
		for z in string:
			if z in vowel:
				for j in range(0,len(string):
					if string[j:j+len(substring)]==substring:
						count_kevin=count_kevin+1
			else:
				for y in range(0, len(string)):
					if string[y:y+len(substring)]==substring:
						count_stuart=count_stuart+1



	if count_kevin > count_stuart:
		print("Kevin", count_kevin)
	else:
		print("Stuart" , count_stuart)

if __name__ == '__main__':
	s=input()
	minion_game(s)