from collections import OrderedDict
od = OrderedDict()
for i in range(int(input())):
  *item, price = input().split()
  item = ' '.join(item)
  od.setdefault(item, 0)
  od[item]=od[item]+int(price)
  print(od)
  
# for k,v in od.items():
#   print('{} {}'.format(k,v))