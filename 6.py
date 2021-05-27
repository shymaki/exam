#Пусть есть массив. Определим скользящую сумму длины i как сумму i последовательных элементов массива. 
#runningSum[i] = sum(nums[0]…nums[i]). Написать программу, возвращающую все скользящие суммы длины i для массива длины n. 
#Массив задается случайно. i и n вводятся с клавиатуры.

from random import randint

n=int(input())
i=int(input())
a=[randint(1, 10) for i in range(n)]
print(a)
print()
b=[0 for i in range(n)]
b[0]=a[0]
for j in range (1, n):
    b[j]=b[j-1]+a[j]
print(b[i-1])
for j in range (1,n-i+1): 
    print(b[j+i-1]-b[j-1])
