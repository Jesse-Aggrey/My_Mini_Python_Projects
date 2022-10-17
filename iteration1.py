a = [1,2,3,4,5]
b = 1
c = 5
d = 5
while a:
    print("This is an iteration:", b, c, d)
    b += 1
    c -= 1
    d = b * c
    print(a)
    a.pop()