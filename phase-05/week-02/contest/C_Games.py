"""

PASSED
"""

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    a = b = 0
    arr.sort(reverse=True)

    for i in range(n):
        if not i % 2:
            if not arr[i] % 2:
                a += arr[i]
        else:
            if arr[i] % 2:
                b += arr[i]

    if a > b:
        print('Alice')
    elif a < b:
        print('Bob')
    else:
        print('Tie')