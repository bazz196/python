user_name = input("What is Your name?: ")
age = int(input("How old are You?: "))

if 70 < age < 90:
    print("You are lucky", user_name, "and welcome.")
elif age > 121:
    print("You are not real", user_name, ".")
elif age > 16:
    print("Welcome", user_name, "on our website.")
elif age == 16:
    print("Dear", user_name, "need to wait one year.")
else:
    print(" I'm sorry", user_name, "you are too young.")

"""
Задача 1.
Написать программу которая будет спрашивать у пользователя имя и возраст.
Проверять
если возраст более 16 вывести Welcome < user_name> on our website.
еcли возраст равен 16 вывести Dear < user_name> need to wait one year.
если возраст между 70 и 90 вывести You are lucky < user_name> and welcome.
если возраст более 121 вывести You are not real < user_name>.
и в конце, если ни одно из условий не удовлетворенно то вывести I'm sorry < user_name>
you are too young.
"""
