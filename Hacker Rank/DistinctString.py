import collections

n = int(input())

d = collections.OrderedDict()
print(d)
for i in range(n):
    word = input()
    if word in d:
        d[word]+= 1
    else:
        d[word]=1
        print("New insert:",d)

print(len(d))

for key in d:
    print(''.join(str(d[key])), end=' ')