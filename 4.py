#Случайный массив из натуральных чисел не превышающих 10, длина массива вводится с клавиатуры. 
#Вернуть число, являющееся результатом последовательного попарного XOR всех элементов массива. Например, XOR([2, 5, 6]) = 2 XOR 5 XOR 6 = 1 


from random import randint

n=int(input())
a=[randint(1, 10) for i in range(n)]
for i in range (n):
    print(a[i])
su=a[0]; 
for i in range (1, n):
    su=su^a[i]; 
print(su)
