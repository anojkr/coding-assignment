def binary_search(list, low, high, item):
    while low <= high:
        mid = (low + high) // 2

        if list[mid] < item:
            low = mid + 1
        elif list[mid] > item:
            high = mid - 1
        else:
            return mid

    return -1


l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(binary_search(l, 0, len(l), 10))
