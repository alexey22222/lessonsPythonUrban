list_cipher = []
list_devider = []
while True:
    str_n = input("Введите число от 3 до 20: ")
    if str_n.isdigit() and int(str_n) >= 3 and int(str_n) <= 20:
        number = int(str_n)
        for i1 in range(3, (number + 1)):
            if number % i1 == 0:
                list_devider.append(i1)
                continue
        i_number = 0
        for i in range(1, int(number/2) + 1):
            j = 0
            while j < number:
                j = j + 1
                if i_number >= len(list_devider):
                    i_number = 0
                    break
                if (i + j) == list_devider[i_number] and j >= i and i != j:
                   list_cipher.append(i)
                   list_cipher.append(j)
                   i_number += 1
                if (j == number - 1):
                      i_number += 1
                      j = 1
        list_cipher = [str(item) for item in list_cipher]
        result = int(''.join(list_cipher))
        print(result)
        break
    else:
        print("Введенная строка не является числом или не соответствует запрашиваемому диапазону")

