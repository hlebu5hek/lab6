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
    return True

k = int(input("Количество точек:\n"))

dots = []
for i in range(k):
    ans = input("Введите координаты точки через пробел:\n")
    dots.append(list(map(lambda x: float(x), ans.split(' '))))

triangles = []
for i in range(len(dots)):
    for j in range(i+1, len(dots)):
        for k in range(j+1, len(dots)):
            triangles.append([dots[i], dots[j], dots[k]])

k = 0
for t in triangles:
    if(checkTriangle(t)): k+=1

print("Количество возможных треугольников (алгоритм) : ", k)
print()

triangles = list(itertools.combinations(dots, 3))

k = 0
for t in triangles:
    if(checkTriangle(t)): k+=1

print("Количество возможных треугольников (функции itertools) : ", k)
print()
