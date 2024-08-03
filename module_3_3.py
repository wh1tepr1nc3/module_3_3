def print_params(a=1, b='String', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

value_list = ['Russia', 1.4, [3, 2, 1]]
value_dict = {'a': 1.4, 'b': 'Russia', 'c': [3, 2, 1]}
print_params(*value_list)
print_params(**value_dict)

value_list_2 = [8, ['France', 'Germany']]
print_params(*value_list_2, 42)