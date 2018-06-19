numbers = []

for f in range(1, 101):
    numbers.append(f)

myList = [x for x in numbers if x % 2 == 0]
print(*myList, sep = "\n")