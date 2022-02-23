"""
Task3. 5 points
отсортировать словарь по ключам
"""

some_dict = {'Яна': 'директор', 'Вася': 'студент', 'Алекс': 'врач'}
sorted_dict = {}
list_keys = list(some_dict.keys())
list_keys.sort()
for i in list_keys:
    print(f' {i} : {some_dict[i]}') # в условии не понятно что именно нужно сделать, поэтому вывожу отсортированные ключи с их значениями
    sorted_dict.update({i: some_dict[i]}) # и создаю новый словаль с отсортированными значениями по ключам
print(some_dict)
print(f' Вот так выглядит сортированный лист {sorted_dict}')
