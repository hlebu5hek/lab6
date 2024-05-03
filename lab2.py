'''
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона),
сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие
минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)
и целевую функцию для нахождения оптимального  решения.
На плоскости задано К точек. Сформировать все возможные варианты
выбора множества точек из них для формирования всех возможных треугольников.

Только равнобедренные
'''
import itertools
import math

def checkTriangle(l):
    a = math.sqrt((l[0][0] - l[1][0])**2 + (l[0][1] - l[1][1])**2)
    b = math.sqrt((l[2][0] - l[1][0])**2 + (l[2][1] - l[1][1])**2)
    c = math.sqrt((l[0][0] - l[2][0])**2 + (l[0][1] - l[2][1])**2)
    if a >= (b + c): return False
    if b >= (a + c): return False
    if c >= (b + a): return False
    if a == b or b == c or c == a: return True
    return False

ans = input()
dots = []
while ans != '0':
    dots.append(list(map(lambda x: int(x), ans.split(' '))))
    ans = input()

triangles = []
for i in range(len(dots)):
    for j in range(i+1, len(dots)):
        for k in range(j+1, len(dots)):
            triangles.append([dots[i], dots[j], dots[k]])

print(*triangles, sep='\n')

k = 0
for t in triangles:
    if(checkTriangle(t)): k+=1

print("Количество возможных равнобедренных треугольников (алгоритм) : ", k)
print()

triangles = list(itertools.combinations(dots, 3))

print(*triangles, sep='\n')

k = 0
for t in triangles:
    if(checkTriangle(t)): k+=1

print()
print("Количество возможных равнобедренных треугольников (функции itertools) : ", k)
