#Heap implementation starting from index 1
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
    list.insert(0, [-5, -6])#Dummy data added so that heap start from index 1
    index = len(list) // 2
    while index != -1:
        heapify(list, index)
        index -= 1


def decrease_key(list, index, value):
    list.insert(0, [-5, -6])#Dummy data added so that heap start from index 1
    i = index
    if value > list[i][0]:
        print("Error")
    list[i][0] = value
    while i > 1 and list[i // 2][0] > list[i][0]:
        list[i][0], list[i // 2][0] = list[i // 2][0], list[i][0]
        list[i][1], list[i // 2][1] = list[i // 2][1], list[i][1]
        i = i // 2
    list.pop(0)
    return list
