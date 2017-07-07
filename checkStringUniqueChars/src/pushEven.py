def pushEven(a):
    even, odd = 0, len(a)-1

    while even < odd:
        if a[even] % 2 is 0:
            even += 1
        else:
            a[even], a[odd] = a[odd], a[even]
            odd -= 1
    return a

print(pushEven([1,1,1,11,1,2,2,22,2]))
