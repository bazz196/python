"""
Задача_2. 5 баллов
Дан список с повторяющимися значениями необходимо из него удалить все определенные значения используя while цикл.
Входные данные: ['bear', 'milk', 'eg', 'eg', 'eg', 'eg'] удалить все eg
Результат: ['bear', 'milk']
"""
my_list = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
i = 'eg'
while i in my_list:
    my_list.remove(i)
print(my_list)
