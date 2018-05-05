def heapify(list, i):
    left = 2 * i
    right = 2 * i + 1
    smallest = i

    if left < len(list) and list[left] <= list[smallest]:
        smallest = left
    if right < len(list) and list[right] <= list[smallest]:
        smallest = right
    if smallest != i:
        list[i], list[smallest] = list[smallest], list[i]
        heapify(list, smallest)


def build_heap(list):
    list.insert(0, 0)
    index = len(list) // 2
    while index != -1:
        heapify(list, index)
        index -= 1
    list.pop(0)


def decrease_key(list, index, value):
    list.insert(0, 0)
    i = index
    if value > list[i]:
        print("Error")
    list[i] = value
    while (i > 1 and list[i // 2] > list[i]):
        list[i], list[i // 2] = list[i // 2], list[i]
        i = i // 2
    list.pop(0)


def heap_sort(list):
    build_heap(list)
    list.insert(0, 0)
    i = len(list)
    r = []
    while i > 1:
        list[1], list[i - 1] = list[i - 1], list[1]
        i = i - 1
        r.append(list.pop())
        heapify(list, 1)
    list.pop(0)
    print(r)
    return r


l = [101, 50, 60, 80, 70, 65, 40, 25, 15, 16, 19, 5, 8]

heap_sort(l)
