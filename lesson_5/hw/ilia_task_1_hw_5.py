"""
Задача 1. 10 баллов
пользователь вводит пароль первый раз система запоминает и просит повторить пароль проверяет его если нет то
просит повторить. А если совпал то сообщение.
"""

print('Enter Your password: ')
pass1 = input()
print('Repeat Your password: ')
pass2 = input()

while pass1 != pass2:
    print('Passwords mismatch.\nRepeat Your password: ')
    pass2 = input()
else:
    print('Congratulation! Registration successful.')
