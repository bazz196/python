"""
Task 4. 15
Удалить дубликаты из dictionary
пример
Before :
{'id1':{'name': 'Ruslan','class': 1,'subjects' : {'Math', 'Algorithms', 'English'}},
'id2':{'name': 'Mark','class': 2,'subjects' : {'Geometry', 'Java', 'Cooking'}},
id3':{'name': 'Ruslan','class': 1,'subjects' : {'Math', 'Algorithms', 'English'}}}
After:
{'id1':{'name': 'Ruslan','class': 1,'subjects' : {'Math', 'Algorithms', 'English'}},
'id2':{'name': 'Mark','class': 2,'subjects' : {'Geometry', 'Java', 'Cooking'}}
"""

some_dict = {'id1': {'name': 'Ruslan', 'class': 1, 'subjects': {'Math', 'Algorithms', 'English'}},
             'id2': {'name': 'Mark', 'class': 2, 'subjects': {'Geometry', 'Java', 'Cooking'}},
             'id3': {'name': 'Ruslan', 'class': 1, 'subjects': {'Math', 'Algorithms', 'English'}}}

new_dict = {}
for key, value in some_dict.items():
    if value not in new_dict.values():
        new_dict.update({key: value})
print(new_dict)
