#Напишите функцию, которая напечатает введенную с клавиатуры строку в обратном порядке. 
#Функциями reverse, reversed, [::-1] и тому подобным пользоваться нельзя.


def reverse_string(s):
    chars = list(s)
    for i in range(len(s) // 2):
        tmp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = tmp
    return ''.join(chars)
   
   
mystring=input()
print(reverse_string(mystring))
