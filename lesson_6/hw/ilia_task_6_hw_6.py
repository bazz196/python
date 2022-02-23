"""
Task 6. 15 Посчитать общее количество наименований в списке. И только в списках.
Example:
shedule =
{'monday': ['clean house', 'drive car', 'meet with freands'],
'thuesday': None,
'wednesday': ['manicure', 'hammam', 'beer']}
Результат: 6
"""
shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None,
           'wednesday': ['manicure', 'hammam', 'beer']}

new_list = []
for k, v in shedule.items():
    if type(v) == list:
        new_list += v

print(len(new_list))

a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# {'b': 1, 'c': 2, 'e': 3}
b = {}
for k, v in a.items():
    if v != None:
        b.update({k: v})
print(b)
