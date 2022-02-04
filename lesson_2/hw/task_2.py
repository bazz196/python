from pprint import pprint

a, b = 5, 10
my_dict = {
    'c1': a + b,
    'c2': b - a,
    'c3': a - b,
    'c4': a * b,
    'c5': b / a,
    'c6': a / b,
    'c7': a ** b,
    'c8': a is b,
    'c9': a == b,
    'c10': a < b,
    'c11': a != b,
    'c12': a < b and b != a,
    'c13': a is b
}
c14 = b // a
c15 = a % b

c_all = c14, c15

pprint(my_dict)
pprint(c_all)