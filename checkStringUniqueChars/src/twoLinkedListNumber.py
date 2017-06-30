class Node():

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self,data):
        a = Node(data)
        if not self.head:
            self.head = a
        else:
            a.next = self.head
            self.head = a

    def prints(self):
        a = self.head
        while a:
            print(a.data)
            a = a.next

    def convert(self):
        num = ''
        a = self.head
        while a:
            num = str(a.data) + num
            a = a.next
        return int(num)

def addLists(l1, l2, carry):

    # Check final digit 
    if l1 is None and l2 is None and carry is 0:
        return None

    # Store value and add l1 and l2
    value = carry

    if l1:
        value += l1.data
    if l2:
        value += l2.data

    result = Node(value % 10)

    result.next = addLists(None if l1 is None else l1.next,
                    None if l2  is None else l2.next,
                    1 if value >= 10 else 0)
    return result


def main():

    a = LinkedList()
    a.add(9)
    a.add(3)
    a.add(6)
    a.prints()
    print('====================================')
    b = LinkedList()
    b.add(5)
    b.add(6)
    b.add(7)
    b.prints()
    print('====================================')
    bb = addLists(a.head,b.head,0)
    cc = bb
    while(cc):
        print(cc.data)
        cc = cc.next

if __name__ == '__main__':
    main()
