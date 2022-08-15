#変数
from re import A


a = 1
b = "python"
c = [1,2,3]

a = [1,2,3]
print(id(a))

a = [1,2,3]
b = a
print(b)

print(a is b)

a = [1,2,3]
b = a[:]
a[1] = 4
print(a)
print(b)

from copy import copy
a = [1,2,3]
b = copy(a)
print(b is a)

a, b = ('python', 'life')
print(a, b)
(a, b)  = 'python','life'
print((a, b))

[a, b] = ['python', 'life']
print([a, b])

a = b = 'python'
print(a)
print(b)

a = 3
b = 5
a,b = b,a
print(a)
print(b)