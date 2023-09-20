import random

def binarySearch(lst, left, right, target):
    if (left > right):
        return None

    mid = int((right - left) / 2 + left)

    if (lst[mid] == target):
        return mid
    elif (lst[mid] < target):
        return binarySearch(lst, mid + 1, right, target)
    else:
        return binarySearch(lst, left, mid - 1, target)

data = [ random.randint(1, 10) for _ in range(10) ]
data.sort()
print(data)

target = random.randint(1, 10)
print('Searching for ' + str(target))

res = binarySearch(data, 0, len(data) - 1, target)
print('Search result ' + str(res))