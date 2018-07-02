def print_formatted(n):
    # your code goes here
    w = len("{0:b}".format(n))
    for i in range(1,n+1):
        print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))
    

if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)