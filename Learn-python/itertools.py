#https://docs.python.org/3.4/library/itertools.html#module-itertools


l = [(1, 2, 9), (1, 3, 12), (2, 3, 8), (2, 4, 4), (2, 5, 7), (3, 5, 5), (3, 6, 2), (4, 5, 2), (4, 7, 10),
         (5, 6, 11), (5, 7, 2), (6, 8, 4), (7, 8, 4), (7, 9, 3), (8, 9, 13)]

b = ['America', 'Sudan', 'Srilanka', 'Pakistan', 'Nepal', 'India', 'France']

from itertools import groupby, filterfalse, dropwhile, cycle, count, repeat, chain, takewhile, islice, zip_longest
from collections import defaultdict
#NOTE- always use itertools with sorted list if index of element is not issue to your solution

def itertools_groupby_example(list_of_nodes):
	graph = defaultdict(list)
	for key, group in groupby(l, lambda x: x[0]):
			graph[key].append(list(group))
	print(dict(graph))

def itertools_false_filter_example(iterator):
	l = []
	for item in filterfalse(lambda x :x>10, iterator):
		l.append(item)
	print(l)

def itertools_dropwhile_example(iterator):
	l = []
	for item in dropwhile(lambda x: x>10, iterator):
		l.append(item)
	print(l)

def itertools_takewhile_example(iterator):
	l = []
	print(iterator)
	for item in takewhile(lambda x: x>10, iterator):
		l.append(item)
	print(l)

def itertools_cycle_example(iterator):
	for item in cycle(iterator):
		print(item)

def itertools_count_example():
	for item in count(start=1, step=1):
		print(item)

def itertools_repeat_example():
	for item in repeat(10, 5):
		print(3)

def itertools_chain_example(iterator1, iterator2):
	l = []
	for item in chain(iterator1, iterator2):
		l.append(item)
	print(l)

def itertools_islice_example(iterator):
	l = []
	for item in islice(iterator, 0, 10, 2):
		l.append(item)
	print(l)

def itertools_chain_from_iterable_examaple():
	l = []
	for item in chain.from_iterable([[2,3,4],[2,5,6]]):
		l.append(item)
	print(l)

def itertools_zip_longest():
	l1 = ['red', 'orange', 'yellow', 'green', 'blue']
	l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
	l3 = ['a','b','c']

	for item in zip_longest(l1, l2, l3, fillvalue=None):
		print(item)

iterator = [11,15,2,5,8,10,50,8,2,3,90,80,100]
iterator1 = [0,10,20,30,40,50,60,70,80,90,100,5]
iterator2 = ['a','b','c']

#itertools_false_filter_example(iterator1)
#itertools_dropwhile_example(iterator1)
#itertools_cycle_example(iterator1)
#itertools_count_example()
#itertools_repeat_example()
#itertools_chain_example(iterator1, iterator2)
#itertools_takewhile_example(iterator)
#itertools_islice_example(iterator)
#itertools_chain_from_iterable_examaple()
#itertools_zip_longest()