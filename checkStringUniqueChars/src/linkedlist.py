import sys

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
    def hasNext(self):
        return self.next is not None

class LinkedList(object):

    def __init__(self):
        self.head = None
    def add(self, data):
        node = Node(data)
        if(self.head is None):
            self.head = node

        else:
            node.next = self.head
            self.head = node


    def prints(self):
        a = self.head
        while(a.data):
            sys.stdout.write(str(a.data) + ",")
            a = a.next
        print("")
def main():
    a = LinkedList()
    a.add(5)
    a.add(4)
    a.add(3)
    a.add(2)
    a.add(1)
    k = 1
    b = a.head
    c = a.head
    while(k > 0):
        b = b.next
        k = k-1
    while(b):
        b = b.next
        c = c.next
    print(c.data)







if __name__ == '__main__':
    main()
