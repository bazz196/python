'''
Задача 2. 15 баллов
Написать программу, которая подсчитывает количество символов в строке
и формирует dict в котором key = буква, value= количество их в слове:
Входная строка : 'Hillel school'
Результат :  {'H': 1, 'i': 1, 'l': 3, 'e': 1, ' ': 1, 's': 1, 'c': 1, 'h': 1, 'o': 2}
'''
# Кстати в условии ошибка - 'l': 3, этих букв 4

import collections
# Первый вариант
input_string = 'Hillel school'  # Определяем переменную со строкой
my_dict = dict(collections.Counter(input_string))  # считаю символы и записываю в переменную результат в формате словаря
print(type(my_dict))  # вывожу тип переменной
print(my_dict)  # вывожу результат

# Второй компактный вариант
input_string = 'Hillel school'
print(dict(collections.Counter(input_string)))

# Третий однострочный вариант
print(dict(collections.Counter('Hillel school')))

