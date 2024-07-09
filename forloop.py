num = int(input("Enter the number of inputs: "))

# Increasing pattern
for i in range(num):
    for j in range(i + 1):
        print('*', end="")
    print()  # New line after each row

# Decreasing pattern
for i in range(num - 1, 0, -1):
    for j in range(i):
        print('*', end="")
    print()  # New line after each row
