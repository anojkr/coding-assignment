def seletion_sort(list):
    for i in range(len(list)):
        minimum = i
        for j in range(i + 1, len(list)):
            if list[j] < list[minimum]:
                minimum = j
        list[minimum], list[i] = list[i], list[minimum]


def run():
    n = int(input())
    l = [int(x) for x in input().split(" ")]
    seletion_sort(l)
    l = [str(i) for i in l]
    s = " ".join(l)
    print(s)

run()
