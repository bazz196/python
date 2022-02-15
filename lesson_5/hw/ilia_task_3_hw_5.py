"""
Задача_3. 10 баллов
Тема while and else
дан список произвольный с int нужно вывести "all numbers are even" если все четные и NO если нет
Пример входных данных: [11, 23, 65, 44, 76, 533]
Результат: NO
Пример входных данных: [12, 22, 66, 44, 76, 534]
Результат: all numbers are even
"""

my_list = [12, 22, 66, 44, 76, 534]
i = 0
while i < len(my_list):
    if my_list[i] % 2 == 0:
        i += 1
    if not i < len(my_list):
        print('all numbers are even')
        break
    if my_list[i] % 2 != 0:
        print('NO')
        break
