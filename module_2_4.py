numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes, not_primes = [], []
cut = 1
for dividend in numbers[1:]:
    is_prime = True
    for divisor in numbers[1:cut]:
        if dividend == divisor:
            continue
        elif dividend % divisor == 0:
            is_prime = False
            break
    if(is_prime):
        primes.append(dividend)
    else:
        not_primes.append(dividend)
    cut += 1
print(f'Primes: {primes}\nNot Primes: {not_primes}')

