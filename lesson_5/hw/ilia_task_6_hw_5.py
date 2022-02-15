set1 = {1, 2, 3}
# add
set1.add(4)
# update
set1.update([2, 3, 4, 5])
# discard
set1.discard(4)
# remove
set1.remove(2)
# copy
set2 = set1.copy()
# pop
set1.pop()
# intersection_update
# set1.difference_update("1", set1)

print(set1)
print(set2)
### set.update(other, ...); set |= other | ... - объединение.
# set.intersection_update(other, ...); set &= other & ... - пересечение.
# set.difference_update(other, ...); set -= other | ... - вычитание.
# set.symmetric_difference_update(other); set ^= other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
### set.add(elem) - добавляет элемент в множество.
### set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует.
### set.discard(elem) - удаляет элемент, если он находится в множестве.
### set.pop() - удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
# set.clear() - очистка множества.'''


"""
Задача_6 5 балллов
Написать примеры всех методов из set объекта.
Пример
set1 = {1,2,3}
# add
set1.add(4)
# update
set1.update([2,3,4,5])
"""
'''
'add',
 'clear',
 'copy',
 'difference',
 'difference_update',
 'discard',
 'intersection',
 'intersection_update',
 'isdisjoint',
 'issubset',
 'issuperset',
 'pop',
 'remove',
 'symmetric_difference',
 'symmetric_difference_update',
 'union',
 'update']'''
'''С множествами можно выполнять множество операций: находить объединение, пересечение...

len(s) - число элементов в множестве (размер множества).
x in s - принадлежит ли x множеству s.
set.isdisjoint(other) - истина, если set и other не имеют общих элементов.
set == other - все элементы set принадлежат other, все элементы other принадлежат set.
set.issubset(other) или set <= other - все элементы set принадлежат other.
set.issuperset(other) или set >= other - аналогично.
set.union(other, ...) или set | other | ... - объединение нескольких множеств.
set.intersection(other, ...) или set & other & ... - пересечение.
set.difference(other, ...) или set - other - ... - множество из всех элементов set, не принадлежащие ни одному из other.
set.symmetric_difference(other); set ^ other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
set.copy() - копия множества.
И операции, непосредственно изменяющие множество:

set.update(other, ...); set |= other | ... - объединение.
set.intersection_update(other, ...); set &= other & ... - пересечение.
set.difference_update(other, ...); set -= other | ... - вычитание.
set.symmetric_difference_update(other); set ^= other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
set.add(elem) - добавляет элемент в множество.
set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует.
set.discard(elem) - удаляет элемент, если он находится в множестве.
set.pop() - удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
set.clear() - очистка множества.'''
