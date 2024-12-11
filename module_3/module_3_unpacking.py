def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params('test')
print_params(40,['one', 'two'])
print_params(11,False,3)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [12, 'string', False]
values_dict = {'a' : '20', 'b' : 'строка_словарь', 'c' : True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['home', [23, 54]]
print_params(*values_list_2,42)


