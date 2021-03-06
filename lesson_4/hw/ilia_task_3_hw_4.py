'''
Задача 3. 15 баллов
Тема list и его методы. Строки и срезы.
Программа принимает список продуктов и принтит самое длинное слово и его длину.
Использовать ''.format() для вывода строки и аргументов.
Входные данные: ['bread', 'milk', 'kolbasa']
Результат: 'Самое длинное название продукта kolbasa длинна 7 символов'
'''

input_list = ['bread', 'milk', 'kolbasa']  # Определяем лист с исходными данными
word = str(max(input_list, key=lambda s: (len(s), s)))  # Нахожу самое длинное слово в листе и записываю как строку
word_length = len(word)  # высчитываю длину слова
print('Самое длинное название продукта {} длинна {} символов '.format(word, word_length))  # Вывожу результат

# Компактный вариант
word, word_length = str(max(['bread', 'milk', 'kolbasa'], key=lambda s: (len(s), s))), len(word)
print('Самое длинное название продукта {} длинна {} символов '.format(word, word_length))


