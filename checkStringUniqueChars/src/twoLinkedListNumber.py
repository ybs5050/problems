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

def main():

    a = LinkedList()
    a.add(7)
    a.add(1)
    a.add(6)
    print(a.convert())

if __name__ == '__main__':
    main()
