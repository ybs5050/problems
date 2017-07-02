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
        iss = 0
        while(a):
            print(a.data)
            a = a.next

def checkLoop(head):

    firstRunner = head
    secondRunner = head

    # firstRunner moves 2 node, secondRunner moves 1 node
    # They will collide eventually if there exists a loop
    while(firstRunner and firstRunner.next):
        secondRunner = secondRunner.next
        firstRunner = firstRunner.next.next
        if secondRunner.data == firstRunner.data:
            print("found")
            break

    # Loop does not exist
    if firstRunner is None or secondRunner is None:
        return None

    # Set secondrunner to head
    # Move both runners 1 node at a time
    # They will collide eventually and the colliding node is where the loop starts
    secondRunner = head
    while(secondRunner.data is not firstRunner.data):
        secondRunner = secondRunner.next
        firstRunner = firstRunner.next

    return secondRunner.data


def main():

    a = LinkedList()
    a.head = Node(1)
    a.head.next = Node(2)
    a.head.next.next = Node(3)
    a.head.next.next.next = Node(4)
    a.head.next.next.next.next = a.head.next
    print(checkLoop(a.head))

if __name__ == '__main__':
    main()
