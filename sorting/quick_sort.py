def partition(list, start, end):
    i = start + 1
    piv = list[start]

    for t in range(start + 1, end):
        if list[t] < piv:
            list[i], list[t] = list[t], list[i]
            i += 1
    list[start], list[i - 1] = list[i - 1], list[start]
    return i - 1

def quick_sort(list, start, end):
    if start < end:
        pivot = partition(list, start, end)
        quick_sort(list, start, pivot - 1)
        quick_sort(list, pivot + 1, end)


def check():
    n = int(input())
    l = [int(x) for x in input().split(" ")]
    quick_sort(l,0, n-1)
    l = [str(i) for i in l]
    s = " ".join(l)
    print(s)

def run():
    n = int(input())
    l = [int(x) for x in input().split(" ")]
    quick_sort(l, 0, n)
    l = [str(i) for i in l]
    s = " ".join(l)
    print(s)

run()