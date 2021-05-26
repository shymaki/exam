#Есть массив из случайных натуральных чисел. Вывести на экран все числа, которые встречаются в нем единожды.

from random import random
N = int(random()*20)
a = [0] * N
for i in range(N):
    a[i] = int(random()*15)
    print(a[i],end=' ')
print()
for i in range(N):
    f = True
    for j in range(N):
        if a[i] == a[j] and i != j:
            f = False
            break
    if f == True:
        print(a[i],end=' ')
print()
