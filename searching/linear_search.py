def linear_search(list, item):
    for t in list:
        if t == item:
            return True
    return False


def linear_search_item_index(list, item):
    for t in range(len(list)):
        if list[t] == item:
            return t
    return -1


l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(linear_search(l, 55))
print(linear_search_item_index(l, 20))
