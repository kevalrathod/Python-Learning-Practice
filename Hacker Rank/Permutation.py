from itertools import permutations
def Permutation():
    a,b = input().split()
    for c in permutations(sorted(a), int(b)):
        print(c)