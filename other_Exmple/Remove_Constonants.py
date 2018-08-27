# def removeConsonant(n):
# 	vovel=['a','e','i','o','u']
# 	word=n.split(" ")
# 	print(word)
# 	for i in word:
# 		if i not in vovel:
# 			n=n.replace(i,"")
# 	# for i in n:
# 	# 	if l in word:
# 	# 		print("mathch",i)


# if __name__ == '__main__':
# 	n=input()
# 	removeConsonant(n)

def eliminate_consonants(x):
        vowels= ['a','e','i','o','u','A','E','I','O','U']
        for char in x:
            if char not in vowels:
                # print(char,end = "")
                x=x.replace(char,"")
        print(x,0end=" ")
eliminate_consonants('mississippi HEllO World')