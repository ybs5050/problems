class SetOfStacks:

    '''
    Create a stack of stacks
    if a stack's size goes over a limit create another stack
    pop() and push() should work as if there is only one stack O(1)
    '''

    def __init__(self):

        self.stack = [[]]
        self.limit = 5
        self.current = 0
        self.size = 0

    def push(self, data):

        if self.current < self.limit:
            self.stack[-1].append(data)
            self.current += 1
            self.size += 1
        else:
            self.stack.append([data])
            self.current = 1
            self.size += 1

    def pop(self):

        if self.size is 0:
            print("None")
        elif self.current is 1:
            self.stack.pop()
            self.current = self.limit
            self.size -= 1
        else:
            self.stack[-1].pop()
            self.current = self.current - 1
            self.size -= 1

    def prints(self):
        print(self.stack)

def main():

    a = SetOfStacks()
    a.push(1)
    a.push(2)
    a.push(3)
    a.push(4)
    a.push(5)
    a.push(6)
    a.push(7)
    a.push(8)
    a.push(9)
    a.push(10)
    a.push(11)
    a.push(12)
    a.push(13)
    a.push(14)
    a.push(15)
    a.push(16)
    a.push(17)
    a.pop()
    a.prints()
    a.pop()
    a.prints()
    a.pop()
    a.prints()
    a.pop()
    a.prints()
    a.pop()
    a.prints()
    a.pop()
    a.prints()
    a.pop()
    a.prints()
    a.pop()
    a.prints()
    a.pop()
    a.prints()
    a.pop()
    a.prints()
    a.pop()
    a.prints()
    a.pop()
    a.prints()
    a.pop()
    a.prints()
    a.pop()
    a.prints()
    a.pop()
    a.prints()
    a.pop()
    a.prints()
    a.pop()
    a.prints()

if __name__ == '__main__':
    main()
