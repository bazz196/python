import datetime

now = datetime.datetime.now()
current_year = now.year
birth_year = input("Pls enter year of Your birth: ")

if birth_year.isdigit() == False:
    birth_year = input("Pls enter year of Your birth without any letters: ")
else:
    birth_year = int(birth_year)

birth_year = int(birth_year)
user_age = current_year - birth_year
print("Great! You age is", user_age)

if user_age == 21:
    print('You should visit Holland.')
elif user_age > 21:
    print('You should visit Vietnam.')
else:
    print('Travel everywhere')

"""
Спросить у пользователя год рождения.
Спомощью if -elif-else
Проверить встроенным строковым методом, состоит ли возраст из числа или текста.
если текст то по попросить ввести число.
Если 21 год вывести “You should visit Holland.”
Если больше 21 вывести “You should visit Vietnam.”
Все остальные варианты. Вывести “Travel everywhere”

"""
