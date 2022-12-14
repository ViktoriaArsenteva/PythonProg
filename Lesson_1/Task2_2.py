# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math


print('Введите значения координат для точки A:')
x1 = int(input('x = '))
y1 = int(input('y = '))
print('Введите значения координат для точки B:')
x2 = int(input('x = '))
y2 = int(input('y = '))
result = math.sqrt((x2 - x1)** 2 + (y2-y1)** 2)
print('Расстояние между точками A (',x1,',',y1,') и B (',x1,',',y1,') = ',round(result,2))