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

def palindrome(aa):
    fast = aa.head
    slow = aa.head
    stack = []

    # Slow move by 1, Fast move by 2
    # 1->2->2->1. Fast will be null, Slow will be 2(pos = 1)
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    # If fast is not null after the while loop
    # The LinkedList has an odd # of nodes
    # Ignore center node by moving slow by 1 node
    if fast:
        slow = slow.next

    while slow:
        if slow.data is not stack[-1]:
            return False
        else:
            stack.pop()
            
        slow = slow.next

    return True

def main():

    a = LinkedList()
    a.add(1)
    a.add(2)
    a.add(3)
    a.add(2)
    a.add(1)
    print(palindrome(a))


if __name__ == '__main__':
    main()
