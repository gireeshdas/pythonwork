def bubblesort(elements):
    for n in range(len(elements) - 1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
        if not swapped:
            return

elements = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is,")
print(elements)
bubblesort(elements)
print("Sorted Array is, ")
print(elements)

sortedelements=sorted(elements)
print("sorted elements :",sortedelements)