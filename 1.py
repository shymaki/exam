#С клавиатуры вводится целое число n. Вернуть строку состоящую из n символов, такую что символы, входящие в строку, повторяются нечетное количество раз. 
#При каждом запуске программы строка должна быть разная ;)


from random import randint

n=int(input())
s='' 
a=randint(0, 9); 
if(n%2==1):
    for i in range (n):
        s=s+str(a)
else:
    b=randint(0, 9)
    if(a==b): 
        b+=1 
    for i in range (n//2): 
        s=s+str(a) 
    for i in range (n//2, n): 
        s=s+str(b)
print(s)
