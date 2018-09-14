def checkPrime(number):
    if number == 2:
        print(number, 'is a Prime Number')
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(number, 'is not a Prime Number')
                break
            else:
                print(number, "Number is Prime number ")

if __name__ == '__main__':
    n = int(input('Enter a number to check: '))
    checkPrime(n)