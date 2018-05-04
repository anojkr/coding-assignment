def heapify(list, i):
    left = 2*i
    right = 2*i+1
    smallest = i

    if left < len(list) and list[left] <= list[smallest]:
        smallest = left
    if right < len(list) and list[right] <= list[smallest]:
        smallest = right
    if smallest != i:
        list[i], list[smallest] = list[smallest], list[i]
        heapify(list, smallest)

def build_heap(list):
    index = len(list)//2
    while index!=-1:
        heapify(list, index)
        index -= 1