first = input("First = ")
second = input("Second = ")
third = input("Third = ")
if first == second and second == third:
    print(f'Вывод: 3')
elif first == second or first == third or second == third:
    print(f'Вывод: 2')
else:
    print(f'Вывод: 0')
