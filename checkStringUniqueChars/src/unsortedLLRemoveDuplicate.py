
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    head = Node(None)
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
        while(a):
            print(a.data)
            a = a.next

def main():
    aa = LinkedList()
    aa.add(5)
    aa.add(3)
    aa.add(3)
    aa.add(3)
    aa.add(3)
    aa.add(3)
    aa.add(3)
    aa.add(11)
    aa.add(11)
    aa.add(11)
    aa.add(11)
    aa.add(11)
    aa.add(11)
    aa.add(55)
    aa.add(55)
    aa.add(55)
    aa.add(55)
    aa.add(3)
    aa.add(11)
    aa.add(11)
    aa.add(11)
    aa.add(11)
    aa.add(11)
    aa.add(11)
    aa.add(55)
    aa.add(55)
    aa.add(55)
    aa.add(55)
    #############
    ###############
    bb = removeDuplicate(aa)
    bb.prints()

def removeDuplicate(list):
    maps = dict()
    aa = LinkedList()
    head = list.head
    while(head):
        if head.data not in maps.keys():
            maps[head.data] = True
            aa.add(head.data)
            head = head.next
        else:
            head = head.next
    return aa

if __name__ == '__main__':
    main()
