#Пусть есть случайный массив из натуральных чисел. Длина массива и максимальное число вводятся с клавиатуры. 
#Напишите программу, которая печатает на экран массив и добавляет True тогда и только тогда, когда все элементы массива уникальны. 


from random import randint

def uni(a):
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                return 0
                quit()
    return 1


n = int(input())
m = int(input())

a = [randint(1, m) for i in range(n)]
print (a)
if uni(a)==1:
    print(a)
    print(True)
