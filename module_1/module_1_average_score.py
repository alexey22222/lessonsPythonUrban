grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
average_score = {}
i = 0
while i < len(students):
    temp = sum(grades[i])/grades[i].__len__()
    average_score.update({students[i]:temp})
    i = i + 1
print(average_score)
