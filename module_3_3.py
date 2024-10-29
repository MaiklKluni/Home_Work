def print_params(a = 1, b = 'строка', c = True):
    print(f"{a}, {b}, {c}")

values_list = [True, 15.35, 'Строка' ]
values_dict = {'a': '54.32', 'b': [12, 24, True], 'c': 54}
values_list_2 = [54.32, 'Строка' ]
print_params()
print_params(5, 'Нет строки', False)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)