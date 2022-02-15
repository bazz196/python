'''
Задача 6. 5 баллов
Тема Кортеж и работа с ним.
Удалить элемент из кортежа.
Входные данные: (1, 2, 3)
Результат: (1, 2)
'''

my_tuple = (1, 2, 3)
first_elem, second_elem, *other_elements = my_tuple
new_tuple = first_elem, second_elem
print(new_tuple)

