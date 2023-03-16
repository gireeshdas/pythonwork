row = int(input("Enter diamond's height: "))
for i in range(row):
    print(" " * (row - i), "*" * (2*i + 1))
for x in range(row - 2, -1, -1):
    print(" " * (row - x), "*" * (2*x + 1))