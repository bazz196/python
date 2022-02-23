"""
Task 5. 10
Вернуть из dictionary все уникальные values.
Пример
Входные данные = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Результат = {'S001', 'S005', 'S007', 'S002', 'S009'}
Усложнение!
Вернуть ту же структуру.

После dictionary L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S005"}, {"V":"S009"},{"VIII":"S007"}]
вернуть из dictionary все уникальные values.
Пример
До dictionary L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
После dictionary L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S005"}, {"V":"S009"},{"VIII":"S007"}]
"""

"""

В общем сделал только первый вариант, со вторым чет таки не поперло.
"""

L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

new_dict = {}
new_list = []
new_set = set()
sorted_dict = {}
for v in L:
    for key, value in v.items():
        # if value not in new_set:
        new_set.add(value)
print(f'Отфильрованный set - {new_set}')


for v2 in L:
    for key, value in v2.items():
        if value not in new_list:
            new_list.append({key: value})
print(new_list)

#
# print(new_list)
# print(new_dict)
# some_dict = dict([{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}])
# new_data = {d.['name']: d for d in some_dict.values()}#.values()
# print(type(new_data))

