#Дана матрица (список списков). Написать программу, которая транспонирует матрицу. 
#Поворачивает ее относительно диагонали


def transpouse(mat):
    matrix = []
    for i in range(len(mat[0])):
        matrix.append(list())
        for j in range(len(mat)):
            matrix[i].append(mat[j][i])
    return matrix
    
n = int(input()) 
a = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)
        
print(a)
print(transpouse(a))
