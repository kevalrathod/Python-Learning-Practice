number=int(input("Enter number:"))
temp=number
reverse=0
while(number>0):
    modulo=number%10
    reverse=reverse*10+modulo
    number=number//10
if(temp==reverse):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")