#Заданы два случайных массива. Напечатать на экран их пересечение. Встроенными в модуль collections методами или иными пользоваться нельзя.

from random import randint

n1 = int(input())
a = [randint(1, 50) for i in range(n1)]
print(a)
n2 = int(input())
b = [randint(1, 50) for i in range(n2)]
print(b)
c = []
for i in a:
    if i in c:
        continue
    for j in b:
        if i == j:
            c.append(i)
            break

print(c)
