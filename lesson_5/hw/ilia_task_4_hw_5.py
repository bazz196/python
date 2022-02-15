"""
Задача_4 25 баллов
написать программу которая будет создавать список методов из доступных методов питон объектов. Под доступными подразумевается
методы без подчеркиваний. Фунции dir()
т.е для объекта set должен быть список методов
['add', 'clear', 'copy', 'difference', 'discard', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'union', 'update']
"""

my_list = list(dir(set))

for i in range(len(my_list) - 1, -1, -1):
    if '__' in my_list[i]:
        del my_list[i]
print(my_list)
