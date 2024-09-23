def print_params(a=1, b='строка', c=True):
    print(a, b, c)

values_list = [5, True, 'lesson']
values_dict = {'a': 2, 'b': 4, "c": 6}
values_list_2 = [8, "name"]

print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)