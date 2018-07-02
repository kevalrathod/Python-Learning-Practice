
def minion_game(string):
    # your code goes here
    kevin=0
    stuart=0
    n=len(string)
    for i in range(0,len(string)):
        if string[i] in {'A','E','I','O','U'}:
            kevin=kevin+n-i
        else:
            stuart=stuart+n-i

    if kevin>stuart:
        print('Kevin',kevin)
    elif kevin==stuart:
        print('Draw')
    else:
        print('Stuart', stuart)


if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
