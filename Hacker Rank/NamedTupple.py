from collections import namedtuple
sum_total=0
N=int(input())
tpl=input().split()
for i in range(N):
    students=namedtuple('student', tpl)
    tpl1,tpl2,tpl3,tpl4 = input().split()
    student =students(tpl1,tpl2,tpl3,tpl4)
    sum_total=sum_total+int(student.MARKS)

print("%.2f"% (sum_total/N))