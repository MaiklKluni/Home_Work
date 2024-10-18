import random

# функция преобразования пары чисел в ключ
def Key(num_st, num_ed):
    digits = len(str(num_ed)) # определяем разряд (длину) числа
    num_st = num_st * (10 ** digits) # Увеличиваем num_st умножения на 10 в степени (digits)
    num_st += num_ed # формируем ключ
    return num_st

first_field = random.randrange(3,20)
numbers = list(range(1, 21))
keys = []
cut = 1
for first_term in numbers:
    for  second_term in numbers[cut:]:
        if first_field % (first_term + second_term) == 0:
           keys.append(Key(first_term, second_term))
    cut += 1

print(f'{first_field} - {keys}')


