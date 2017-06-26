# check if a rotated string is a
# subscript of another string

def isRotation(s1,s2):
    l = len(s1)
    if(l is len(s2) and l > 0):
        s = s1 + s1 # hello -> hellohello
        return s2 in s
    return False

s2 = "llohe" #hello is rotated
s1 = "hello"

print(isRotation(s1,s2))
