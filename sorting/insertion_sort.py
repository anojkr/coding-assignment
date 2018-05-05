def insertion_sort(list, n):
	for t in range(0,n):
		temp = list[t]
		j = t

		while j>0 and temp<list[j-1]:
			list[j] = list[j-1]
			j=j-1

		list[j] = temp

def run():
    n = int(input())
    l = [int(x) for x in input().split(" ")]
    insertion_sort(l, n)
    l = [str(i) for i in l]
    s = " ".join(l)
    print(s)

run()