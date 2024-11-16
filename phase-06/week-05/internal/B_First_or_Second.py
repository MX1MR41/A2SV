"""
PASSED

"""

n1, n2, k1, k2 = list(map(int, input().split()))

turn = True
while n1 and n2:
    if turn:
        n1 -= 1
    else:
        n2 -= 1

    turn = not turn

if n2:
    print("Second")
else:
    print("First")
