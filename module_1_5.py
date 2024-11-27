immutable_var = (3,7,"hi", True, False, 12.1, [1,3,7])
print(immutable_var)
immutable_var[0] = 78 # в кортеже содержится ссылки на элементы(объекты), они неизменяемые
mutable_list = [4,7,"test", True,[2,6], "version_3"]
mutable_list[1] = 10
mutable_list[3] = False
mutable_list[-1] = "version_4"
print(mutable_list)
