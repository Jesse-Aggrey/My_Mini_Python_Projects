a = [1,2,3,4,5]                             # list a
b = 1
c = 5
d = 5
while a:
    print("This is an iteration:", b, c, d)
    b += 1                                  # increase variable b by 1 at each iteration
    c -= 1                                  # decrease variable c by 1 at each iteration
    d = b * c                               # result d as product of b and c
    print(a)
    a.pop()                                 # remove last character from the list at each iteration