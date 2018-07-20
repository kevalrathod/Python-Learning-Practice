# import re

# m=re.findall(r'\w' ,'hackerrank129/')
# print(m)

import re
m=re.search(r'\d+','abccdd')
print(m.start())
print(m.end())