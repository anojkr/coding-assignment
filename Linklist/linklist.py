from sorting import merge_sort


class Linklist:
    def __init__(self, data, nextnode=None):
        self.data = data
        self.nextnode = nextnode

    def traverse(self):
        r = []
        while self != None:
            r.append(self.data)
            self = self.nextnode
        print("Link-List  {}".format(r))
        return r

    def add_node_middle(self, data, set_data):
        if self != None:
            while self.data != data:
                self = self.nextnode
            X = Linklist(set_data)
            X.nextnode = self.nextnode
            self.nextnode = X
        else:
            print("Error")

    def add_node_begining(self, data):
        if self != None:
            X = Linklist(data)
            X.nextnode = self
            self = X
        return X

    def add_node(self, *data):
        node = self
        if node != None:
            while node.nextnode != None:
                node = node.nextnode
            for t in data:
                X = Linklist(t)
                node.nextnode = X
                X.nextnode = None
                node = X

    def delete_node(self, *data):
        node = self
        if node != None:
            for t in data:
                while node.nextnode.data != t:
                    node = node.nextnode
                node.nextnode = node.nextnode.nextnode
                node = self

    def delete_head(self):
        node = self
        if node != None:
            node = node.nextnode
        return node


if __name__ == '__main__':
    l = Linklist(10)
    l.add_node(20, 5, 15, 40, 80, 60, 50)
    x = l.traverse()
    result = merge_sort.sortarr(x)
    z = Linklist(result[0])
    z.add_node(*result[1:])
    z.traverse()
