#С клавиатуры вводится строка, содержащая повторяющиеся символы. Написать программу, которая удалит все повторы и напечатает результат на экран.

s = input()
s_new = ''

for i in s:
    if i not in s_new:
        s_new += i
print(s_new)
