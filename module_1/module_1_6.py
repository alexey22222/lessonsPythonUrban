my_dict = {'Nikita' : 1992, 'Alena' : 2014, 'Alexey' : 1994, 'Bob' : 2004}
print(my_dict)
print(my_dict['Bob'], my_dict.get('Slon'))
my_dict.update({'Varvara' : 1985, 'Ivan' : 2009})
key_delete = my_dict.pop('Alexey')
print(key_delete)
print(my_dict)

my_set = {'test', 'hard', 32, 1, 46, False, 1, False, (1,23,34)}
print(my_set)
my_set.add(90)
my_set.add('Number')
my_set.discard('hard')
print(my_set)
