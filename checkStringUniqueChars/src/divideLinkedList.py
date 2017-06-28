import sys

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    def hasNext(self):
        return self.next is not None

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tailend = None
        self.tailFront = None
    def addFront(self, data):
        node = Node(data)
        if(self.head is None):
            self.head = node
        else:
            if self.tailend is None:
                self.head.next = node
                self.tailend = self.head.next
            else:
                self.tailend.next = node
                self.tailend = self.tailend.next

    def prints(self):
        a = self.head
        while(a):
            print(a.data)
            a = a.next
def main():
    # 5,4,3,2,1 if target = 3, put target <= before target, put target >= after target
    # result: 1,2,3,4,5 or 2,1,3,5,4
    a = LinkedList()
    a.addFront(1)
    a.addFront(2)
    a.addFront(3)
    a.addFront(4)
    a.addFront(5)
    a.addFront(1)
    a.addFront(2)
    a.addFront(3)
    a.addFront(4)
    a.addFront(5)
    a.prints()
    print("-------------------------------")
    target = 3
    b = LinkedList()
    aa = a.head
    while(aa):
        if(aa.data < target):
            b.addFront(aa.data)
        aa = aa.next
    aa = a.head
    while(aa):
        if(aa.data >= target):
            b.addFront(aa.data)
        aa = aa.next
    b.prints()






if __name__ == '__main__':
    main()
