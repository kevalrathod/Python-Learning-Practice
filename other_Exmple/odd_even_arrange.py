#even in even index
#odd in odd in dex


list1 = [5, 7, 6, 8, 10, 3, 4, 9, 2, 1, 12]
odd_list = []
even_list = []
for i in range(len(list1)):
    if((list1[i] % 2) == 0):
        even_list.append(list1[i])
    else:
        odd_list.append(list1[i])
print(list1)
j = 0
k = 0
for i in range(0, len(list1)):
    if((i % 2 == 0) and (j < len(odd_list))):
        list1[i] = odd_list[j]
        j += 1
    elif(k < len(even_list)):
        list1[i] = even_list[k]
        k += 1
print(list1)