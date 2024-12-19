def calculate_structure_sum(data_structure):
    sum = 0
    for i in range(len(data_structure)):
        if isinstance(data_structure[i], int):
            sum = sum + data_structure[i]
        elif isinstance(data_structure[i], str):
            sum = sum + len(data_structure[i])
        elif isinstance(data_structure[i],list):
            sum = sum + calculate_structure_sum(data_structure[i])
        elif isinstance(data_structure[i],tuple):
            sum = sum + calculate_structure_sum(data_structure[i])
        elif isinstance(data_structure[i],dict):
            sum = sum + calculate_structure_sum(list(data_structure[i].values()))
            sum = sum + calculate_structure_sum(list(data_structure[i].keys()))
        elif isinstance(data_structure[i], set):
            sum = sum + calculate_structure_sum(list(data_structure[i]))
    return sum

result = [[1,2,3],{'a':4,'b':5}, (6, {'cube':7,'drum':8}),"Hello", ((),[{(2,'Urban',('Urban2',35))}])]
print(calculate_structure_sum(result))

