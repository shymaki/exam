#С клавиатуры вводятся две строки s1 и s2.
#Написать программу, которая выводит на экран строку, состоящую из последовательных символов из строк идущих поочередно друг за другом. 
#Пробелы игнорируются. Например s1 = “это строка”, а s2 = “а вот еще одна”. Тогда результатом будет строка: “эатвоосттерщоекоадна”

s1=input()
s2=input()
s1=s1.split()
s2=s2.split()
c=[]
b=[]
for i in range (len(s1)):
    s1[i]=list(s1[i])
    c=c+s1[i]
for i in range (len(s2)):
    s2[i]=list(s2[i])
    b=b+s2[i]
print(c)
print(b)
for j in range (min(len(c), len(b))):
    print(c[j], b[j])
for i in range (min(len(c), len(b)), max(len(c), len(b))):
    if len(c)>len(b):
        print(c[i])
    if len(c)<len(b):
        print(b[i])
