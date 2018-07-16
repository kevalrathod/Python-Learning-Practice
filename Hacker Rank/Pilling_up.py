T = int(input())
for i in range(T):
    n = int(input())
    sizes = list(map(int, input().split()))
    x, y = 0, n - 1
    while x < n - 1 and sizes[x] >= sizes[x + 1]:
        x += 1
        print("value of x:",x)
    while y > 0 and sizes[y] >= sizes[y - 1]:
        y -= 1
        print("value of y:",y)
    print('Yes') if x>=y else print('No')