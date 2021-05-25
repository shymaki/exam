#С клавиатуры вводится натуральное число n. Вернуть True, если оно является степенью двух. Иначе False.

a=int(input())
n=1
while n*2<=a:
    n*=2
if n==a:
    print('YES')
else:
    print('NO')
