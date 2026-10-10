def linear_search(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1

values = [12, 7, 25, 4, 18]
target = int(input("Number to find: "))
print("Index:", linear_search(values, target))
