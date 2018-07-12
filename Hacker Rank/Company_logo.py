#COMPANYLOGO

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

if __name__ == "__main__":
    s=input()
    sorted_data=sorted(s)
    list = OrderedCounter(sorted_data).most_common(3)
    for c in list:
        print(*c)