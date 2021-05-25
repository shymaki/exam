#С клавиатуры вводится натуральное число. Вернуть разность между произведением и суммой входящих в него чисел.

n = int(input())

sum = 0
mult = 1

while n > 0:
    digit = n % 10
    sum = sum + digit
    mult = mult * digit
    n = n // 10
    
print(mult-sum)
