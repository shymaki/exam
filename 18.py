#Есть случайный массив из натуральных чисел. Замените каждый элемент из него на наибольший из тех, которые расположены после текущего. 
#Последний элемент заменить на -1. Результат вывести на экран.


from random import randint

n = randint(1, 50)
a = [randint(1, 50) for i in range(n)]
print(a)

for i in range (n):
    if i==(n-1):
        a[i]=-1
    else:
        max = a[i+1]
        for k in range(i+1, n):
            if a[k] > max:
              max = a[k]
        a[i]=max

print(a)
