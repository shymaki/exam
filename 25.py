#Написать программу, выводящую на экран n-ое число Фибоначчи.

a=int(input())

f0=0
f1=1
n=1  

while n<a:
    f0, f1 = f1, f0 + f1
    n+=1 
    
print(f1)
