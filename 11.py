#С клавиатуры вводится строка с координатами квадратика на шахматной доске. Определить по координатам цвет квадратика.

numb = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8'}

a=input()
b=a.split()
b[1]=numb[b[1]]
if (int(b[0])+int(b[1]))%2==0:
    print('Black')
else:
    print('White')
