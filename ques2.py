numbers = [5, 8, 10, 3, 6]
factorials = []
for num in numbers:
    result = 1
    for i in range(1, num + 1):
        result *= i
    factorials.append(result)
print(','.join(map(str, factorials)))
