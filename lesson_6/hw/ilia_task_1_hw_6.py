"""
Task 1. 5 points
сложить словари в один.
использовать for и dict methods.
"""
first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}
my_tuple = first, second, third, fourth, fifth
all_dict = {}

for i in my_tuple:  # вариант через кортеж
    all_dict.update(i)
print(all_dict)

for i in first, second, third, fourth, fifth:  # вариант через словари
    all_dict.update(i)
print(all_dict)
