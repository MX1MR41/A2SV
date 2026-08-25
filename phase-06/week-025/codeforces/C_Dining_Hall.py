"""

https://codeforces.com/problemset/problem/2090/C

"""

def getcells(x, y):
    return [(x+ y , x, y, True), (x + y + 1,x, y + 1, False), (x + y + 1,x + 1, y, False), (x + y + 4, x + 1, y + 1, False)]


def gettables(x):
    return [(x,x - i, i, True) for i in range(x - 1, 0, -1) if not (x - i - 1) % 3 and not (i - 1) % 3]



for _ in range(int(input())):

    n = int(input())
    a = list(map(int, input().split()))

    zeroes = a.count(0)
    ones = n - zeroes

    tables = []
    cells = []

    curr_dist = 2

    while len(tables) < 2*n:
        tables.extend(gettables(curr_dist))
        curr_dist += 3

    for t in tables:
        cells.extend(getcells(t[1], t[2]))

    while len(cells) < 2*n:
        nt = gettables(curr_dist)
        curr_dist += 3
        for t in nt:
            cells.extend(getcells(t[1], t[2]))


    cells.sort(reverse = True)
    tables.sort(reverse = True)

    res = []
    occupied = set()
    for i in range(n):
        g = a[i]
        if g == 0:
            while tables and tables[-1] in occupied:
                tables.pop()

            t = tables.pop()
            occupied.add(t)
            res.append((t[1], t[2]))

        else:
            while cells and cells[-1] in occupied:
                cells.pop()

            c = cells.pop()
            res.append((c[1], c[2]))
            occupied.add(c)
    

    for x, y in res:
        print(x, y)
