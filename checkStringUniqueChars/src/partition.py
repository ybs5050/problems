def partition(a):
    pivot = a[int((len(a)-1)/2)]
    smaller = 0

    for i in range(len(a)):
        if a[i] < pivot:
            a[i], a[smaller] = a[smaller], a[i]
            smaller += 1

    larger = len(a) - 1

    for i in reversed(range(len(a))):
        if a[i] < pivot:
            break
        elif a[i] > pivot:
            a[i], a[larger] = a[larger], a[i]
            larger -=1

    return a

aa = [0,1,2,0,1,2,0,1,2]
print(partition(aa))
