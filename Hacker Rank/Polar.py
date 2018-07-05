import cmath

z = complex(input())
a=abs(z)
b=cmath.phase(z)
print('{"%.3f"%}\n{"%.3f"%}'.format(a,b))
