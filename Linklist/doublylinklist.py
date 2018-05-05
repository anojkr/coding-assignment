from sorting import merge_sort


class Doublylinklist:

    def __init__(self, data, prevnode=None, nextnode=None):
        self.data = data
        self.prev_node = prevnode
        self.next_node = nextnode

    def add_node_end(self, head, *data):
        t = head
        if t != None:
            while t.next_node != None:
                t = t.next_node
            for s in data:
                x = Doublylinklist(s, t)
                t.next_node = x
                x.prev_node = t
                t = x

    def add_node_begin(self, head, data):
        if head != None:
            x = Doublylinklist(data, None, head)
            head.prev_node = x
            head = x
            return head

    def add_node_middle(self, head, data, set_data):
        t = head
        if t != None:
            while t.data != data:
                t = t.next_node
            X = Doublylinklist(set_data, t, t.next_node)
            t.next_node.prev_node = X
            t.next_node = X
        else:
            print("Error")

    def traversal(self, head, start=None):
        t = head
        r = []
        if start == 'end':
            while t.next_node != None:
                t = t.next_node
            while t != None:
                r.append(t.data)
                t = t.prev_node
        else:
            while t != None:
                r.append(t.data)
                t = t.next_node
        print(r)
        return r


head = Doublylinklist(10)
# print(head.data)

head.add_node_end(head, 20, 30, 40, 500, 600, 700, 80, 90, 100)
head = head.add_node_begin(head, 5)

head.add_node_middle(head, 80, 55)
r = head.traversal(head)
print(merge_sort.sortarr(r))
