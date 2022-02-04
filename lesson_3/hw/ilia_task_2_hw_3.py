msg_1 = 'Привет, повелитель!'
msg_2 = 'Советую Вам посмотреть "StarWars" или "Мандалорец"'
msg_3 = 'Советую Вам посмотреть "Трансформеры"'
msg_4 = 'Советую Вам посмотреть "Инсургент"'
msg_5 = 'Советую Вам посмотреть "TENET"'
msg_6 = 'Советую Вам посмотреть "TMNT"'
msg_7 = 'Огромное спасибо!'

print('Hi my dear friend. Tell me please more information about yourself.', 'What your nickname is?', sep='\n',
      end=': ')
user_nickname = input()
if user_nickname == 'admin':
    print('{}'.format(msg_1), 'Are You Ж or М?', sep='\n', end=': ')
else:
    print('Are You Ж or М?', end=': ')
user_gender = input()
print('How old are You?', end=': ')
user_age = int(input())

if 10 < user_age < 14 and user_gender == 'М' and user_nickname == 'Guido':
    print(msg_2, msg_7, sep='\n')
elif user_age > 30 and user_gender == 'М' and user_nickname == 'Guido':
    print(msg_2, msg_7, sep='\n')
elif 22 < user_age < 32 and user_gender == 'Ж' and user_nickname == 'Guido':
    print(msg_3, msg_7, sep='\n')
elif user_age < 16 and user_gender == 'Ж' and user_nickname == 'Guido':
    print(msg_4, msg_7, sep='\n')
elif user_age < 11 and user_gender == 'М' and user_nickname == 'Guido':
    print(msg_6, msg_7, sep='\n')
elif 10 < user_age < 14 and user_gender == 'М':
    print(msg_2)
elif user_age > 30 and user_gender == 'М':
    print(msg_2)
elif 22 < user_age < 32 and user_gender == 'Ж':
    print(msg_3)
elif user_age < 16 and user_gender == 'Ж':
    print(msg_4)
elif user_nickname == 'Женя':
    print(msg_5)
elif user_age < 11 and user_gender == 'М':
    print(msg_6)
else:
    print('Wow! nice to meet you %s, I think that Your age = %s is ok, and that You are %s, is ok too.' % (
        user_nickname, user_age, user_gender))

"""
Задача 2 на 25 балов
Написать программу, которая
Приветствует пользователя в произвольном виде. 
Принимает на ввод его никнейм, пол, возраст. 
Если никнейм содержит admin, выводит: "Привет, повелитель!", не прекращая работу.
Если возраст больше 10 и меньше 14 и пол М или больше 30 и пол М: Выводит "Советую Вам посмотреть "StarWars" или 'Мандалорец'"
Если возраст больше 22 и меньше 32 и пол Ж: Рекомендация "Советую Вам посмотреть "Трансформеры""
Если возраст меньше 16 и пол Ж: Рекомендация "Советую Вам посмотреть "Инсургент""
Если никнейм 'Женя': Рекомендация "Советую Вам посмотреть 'TENET'"
Если возраст до 11 и пол М: Рекомендация "Советую Вам посмотреть "TMNT""
Если никнейм Guido: Кроме рекомендации, выводит "Огромное спасибо!"

Бонус


Использовать в print(sep='', end='')
Использовать в внутри print(переменную из input, sep='', end='')
"""
