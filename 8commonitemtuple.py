tup = (1, 2, 3, 2, 4, 5, 1, 6, 2)
repeated = []

for item in tup:
    if tup.count(item) > 1 and item not in repeated:
        repeated.append(item)

print("Repeated items:", repeated)
