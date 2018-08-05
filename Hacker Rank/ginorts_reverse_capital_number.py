import re
r = re.compile("([a-zA-Z]+)([0-9]+)")
str=r.match(input())
str2=str.group(1)
str3=''.join(sorted(str2))
n=1
str4=str3[n:]+str3[:n]
str5=str.group(2)
odd_str= ' '
even_str=' '
final_str=' '
for i in str5:
    if(int(i)%2!=0):
        odd_str=odd_str+i
    elif(int(i)%2==0):
        even_str=even_str+i
str6=odd_str+even_str
final_str=str4+str6
print(final_str.replace(" " , ""))