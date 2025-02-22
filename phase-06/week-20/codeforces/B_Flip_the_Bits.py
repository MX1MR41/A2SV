"""

https://codeforces.com/problemset/problem/1504/B

"""

for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()

    pre = []
    z = o = 0
    for i in a:
        z += 1 if i == "0" else 0
        o += 1 if i == "1" else 0

        if z == o:
            pre.append(True)
        else:
            pre.append(False)

    flipped = False

    can = True

    for i in range(n-1, -1, -1):
        if not flipped:
            if a[i] != b[i]:
                if pre[i]:
                    flipped = True
                else:
                    can = False

        else:
            if a[i] == b[i]:
                if pre[i]:
                    flipped = False
                else:
                    can = False

    if can:
        print("YES")
    else:
        print("NO")
