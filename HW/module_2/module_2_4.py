numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    perebor = int((i ** 0.5) + 1)
    counter = 0
    for j in range(1, (i + 1)):
        if i % j == 0:
            counter += 1

    if counter == 2:
        primes.append(i)
    elif counter >= 3:
        not_primes.append(i)

print('Primes:', primes)
print('Not Primes:', not_primes)