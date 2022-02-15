'''
Задача 4. 5 баллов
Пользователь водит свое имя.
Возвращается тектс в БОЛЬШОМ и маленьком регистре. Использовать ' '.format().
Для вставки аргументов в текст.
Входные данные: Apollo
Результат: APPOLLO apollo
'''

user_name = input()  # Получаем имя юзера
upper_name, lower_name = user_name.upper(), user_name.lower()
print('ИМЯ - {}, имя - {}'.format(upper_name, lower_name))

