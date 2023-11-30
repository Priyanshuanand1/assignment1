n = int(input("Enter a positive integer value for 'n': "))
result_dict = {}
for i in range(1, n + 1):
    result_dict[i] = i * i
print("Generated Dictionary:", result_dict)
