#reading file and output file 

f=open('myfile.txt','r')
print(f.name())
print(f.mode())
f.close()


#2nd method

with open('myfile.txt','r') as f:
	size=4
	fop=f.read(size)
	while len(fop)>0:
		print(fop,end='*')
		fop=f.read(size)


#copy one file to another

with open('myfile.txt','r') as f:
	with open('mynewtext.txt','w') as w:
		for line in f:
			w.write(line)



