#Случайным образом задается массив натуральных чисел, написать программу, которая возвращает количество элементов массива с четным количеством цифр.

def count(arr, l):
    c = []
    for i in range (l):
        if (len(str(arr[i]))%2==0):
            c.append(arr[i])
    return c
        

k = int(input())
a = []
for i in range (k):
    a.append(int(input()))
    
print(a)

print(count(a, k))
