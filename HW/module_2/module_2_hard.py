import random
n = random.choice(range(3, 21))

collect = []
for i in range(1, n):
    counter = 0
    while counter != n:
        a = counter + 1
        if n % (i + a) == 0 and i != a:
            collect.append([i] + [a])
            for j in range(len(collect)):
                if ([i] + [a])[::-1] in collect:
                    collect.pop()
                    break
        counter += 1

result = []
for lists in collect:
    for num in lists:
        result.append(str(num))

print(n)
print(''.join(result))
