grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#Алгоритм
# 1. Переводим множество в список (list()) и сортируем по алфавиту (sorted() ; .sort())
students = sorted(list(students))
# 2. Находим среднее значение в каждом элементе списка и добавляем в новый (sum; len)
average_score = [int(sum(grades[0]))/len(grades[0]), int(sum(grades[1]))/len(grades[1]), int(sum(grades[2]))/len(grades[2]),
              int(sum(grades[3]))/len(grades[3]), int(sum(grades[4])/len(grades[4]))]
# 3. создаём словарь из двух списков
average_score_of_students = dict(zip(students, average_score))
print(average_score_of_students)

