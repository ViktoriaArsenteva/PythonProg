# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

from random import randint


n = int(input('Введите количество элементов в списке: '))
array = []
for i in range (n):
    array.append(randint(-n,n))
#print('Введите позиции элементов от 0 до',n - 1,'через пробел, чтобы найти их произведение: ')
num = input()
res = 1
for j in num.split( ):
    res *= array[int(j)]
print('Произведение выбранных элементов из списка',array,'=', res)