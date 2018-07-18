n, x = map(int, input().split()) 

sheet = []
for i in range(0,x):
    sheet.append( map(float, input().split())) 
    
for i in zip(*sheet):
    
    print( sum(i)/len(i) )