class Node:

    def __init__(self, data, min):
        self.data = data
        self.next = None
        self.min = min

class StackWithMin:

    # Each node will have its respective min value
    # For example, [3,4] min = 3, [2,3,4] min = 2
    # But node(3)'s min is still 3, and node(4)'s min is still 4

    def __init__(self):
        self.stack = []

    # get new min value
    def push(self, data):
        newMin = min(data, self.min())
        # add new node to stack with new min value
        self.stack.append(Node(data, newMin))

    def min(self):
        if len(self.stack) is 0:
            return float('inf')
        else:
            return self.stack[-1].min

    def printMin(self):
        return self.stack[-1].min

    def pop(self):
        self.stack.pop()

def main():

    a = StackWithMin()
    a.push(5) # Stack[5], min =5
    a.push(6) # Stack[6,5], min = 5
    a.push(3) # Stack[3,6,5], min = 3
    a.push(7) # Stack[7,3,6,5], min = 3
    a.pop() # Stack[3,6,5], min = 3
    a.pop() # Stack[6,5], min = 5
    print(a.printMin())


if __name__ == '__main__':
    main()
