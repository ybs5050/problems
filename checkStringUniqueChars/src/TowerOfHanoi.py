class Tower:
    def __init__(self, i):
        self.disks = []
        self.index= i

    def index():
        return self.index

    def add(self, i):
        if len(self.disks) > 0 and self.disks[-1] <= i:
            print("Error")
        else:
            self.disks.append(i)

    def moveTopTo(self, t):
        top = self.disks.pop()
        t.add(top)
        print('Move Disk ' + str(top) + ' from ' + str(self.index) + ' to ' + str(t.index))


    def moveDisks(self, n, dest, buff):

        # Base case
        if n > 0:
            # Use third tower as buffer and move n-1 plates from Tower 0 to Tower 2
            self.moveDisks(n-1, buff, dest)
            # Move leftover plates from origin to destination
            self.moveTopTo(dest)
            # Move all plates in buffer to destination. Use Tower 0 as a buffer
            buff.moveDisks(n-1, dest, self)

def main():
    n = 3
    towers = []

    for i in range(n):
        towers.append(Tower(i))

    for i in range(n, 0, -1):
        towers[0].add(i)

    # Total # of iteration =  n*2 + 1, n =3; 7
    towers[0].moveDisks(n, towers[2], towers[1])
    for i in towers:
        print(i.disks)

if __name__ == '__main__':
    main()
