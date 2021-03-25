"""
Шайдулина Τамара Μаратοвна
редактируйте/пишите код в блоках между
---начало--- и ---конец---
Решение задачи может быть в несколько строчек, но чем меньше, тем лучше.
В случае верного решения запуск файла приведёт к выводу True для каждого задания
"""
a = 'Шайдулина Τамара Μаратοвна'
""" Задание №1
Запишите в переменную 'fio' список, полученный из переменной 'а' и содержащий Фамилию, Имя, Отчество
---------------начало блока редактирования----------------"""

a = a.split()
fio = list(a)

"""------------ конец блока редактирования----------------"""
print('№1 ' + str(fio == ['Шайдулина', 'Τамара', 'Μаратοвна']))

""" Задание №2
Получите только имя из переменной 'fio' и запишите в переменную 'name'
---------------начало блока редактирования----------------"""

name = fio[1]

"""------------ конец блока редактирования----------------"""
print('№2 ' + str(name == 'Τамара'))

""" Задание №3
Получите в переменной 'l' длину своей фамилии
---------------начало блока редактирования----------------"""

l = len(fio[0])

"""------------ конец блока редактирования----------------"""
print('№3 ' + str(l == 9))

""" Задание №4
Получите в переменной 'res' строку из третей буквы вашей Фамилии
---------------начало блока редактирования----------------"""

b = list('Шайдулина')
res = b[2]

"""------------ конец блока редактирования----------------"""
print('№4 ' + str(res == 'й'))

""" Задание №5
Получите в переменной 'res' строку из двух первых букв вашей Фамилии
---------------начало блока редактирования----------------"""

res = b[0] + b[1]

"""------------ конец блока редактирования----------------"""
print('№5 ' + str(res == 'Ша'))

""" Задание №6
Получите в переменной 'res' строку из двух последних букв вашей Фамилии
---------------начало блока редактирования----------------"""

res = b[7] + b[8]

"""----------- конец блока редактирования----------------"""
print('№6 ' + str(res == 'на'))

""" Задание №7
Получите в переменной 'surname_list' список из букв вашей Фамилии по очереди
---------------начало блока редактирования----------------"""

surname_list = list('Шайдулина')

"""------------ конец блока редактирования----------------"""
print('№7 ' + str(surname_list == ['Ш', 'а', 'й', 'д', 'у', 'л', 'и', 'н', 'а']))

""" Задание №8
Получите в переменной 'surname_tuple' кортеж из букв вашей Фамилии по очереди
---------------начало блока редактирования----------------"""

surname_tuple = tuple('Шайдулина')

"""------------ конец блока редактирования----------------"""
print('№8 ' + str(surname_tuple == ('Ш', 'а', 'й', 'д', 'у', 'л', 'и', 'н', 'а')))

""" Задание №9
Получите в переменной 'res' список чётных чисел от 1 до длины вышей фамилии
---------------начало блока редактирования----------------"""
res = list(range(len('Шайдулина')))
res = res[2::2]
print(res)
"""------------ конец блока редактирования----------------"""
print('№9 ' + str(res == [2, 4, 6, 8]))

""" Задание №10
Получите в переменной 'res' список кортежей где первый элемент кортежа это номер буквы в вашей фамилии (от 0), а второй это буква вашей фамилии
---------------начало блока редактирования----------------"""

res = list()
for i in enumerate(list('Шайдулина')):
	res.append(tuple(i))
print(res)

"""------------ конец блока редактирования----------------"""
print('№10 ' + str(res == [(0, 'Ш'), (1, 'а'), (2, 'й'), (3, 'д'), (4, 'у'), (5, 'л'), (6, 'и'), (7, 'н'), (8, 'а')]))

""" Задание №11
Получите в переменной 'res' из переменной surname_list список букв вашей фамилии наоборот
---------------начало блока редактирования----------------"""
surname_list = list('Шайдулина')
res = list(reversed(surname_list))

"""------------ конец блока редактирования----------------"""
print('№11 ' + str(res == ['а', 'н', 'и', 'л', 'у', 'д', 'й', 'а', 'Ш']))

""" Задание №12
Получите в переменной 'res' из переменной fio строку с вашей фамилией задом наперёд
---------------начало блока редактирования----------------"""
fio = list(a)
res = ''.join(reversed(fio[0]))

"""------------ конец блока редактирования----------------"""
print('№12 ' + str(res == 'анилудйаШ'))

""" Задание №13
Получите в переменной 'res' из переменной surname_list список букв вашей фамилии без третей буквы
---------------начало блока редактирования----------------"""
surname_list = list('Шайдулина')
surname_list.remove(surname_list[2])
res = surname_list

"""------------ конец блока редактирования----------------"""
print('№13 ' + str(res == ['Ш', 'а', 'д', 'у', 'л', 'и', 'н', 'а']))
