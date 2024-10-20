"""

PASSED

"""

from collections import defaultdict

qs = []
_max = 0
for _ in range(int(input())):
    curr = list(map(int, input().split()))
    _max = max(_max, curr[1], curr[2])
    qs.append(curr)


fee = defaultdict(int)


def weight(u, v, w):
    us, vs = [], []
    while u > 1:
        us.append(u)
        u //= 2

    while v > 1:
        vs.append(v)
        v //= 2

    us.reverse()
    vs.reverse()
    ind = 0
    while ind < len(us) and ind < len(vs) and vs[ind] == us[ind]:
        ind += 1

    for i in range(ind, len(us)):
        fee[us[i]] += w
    for i in range(ind, len(vs)):
        fee[vs[i]] += w


def move(u, v):

    us, vs = [], []
    while u > 1:
        us.append(u)
        u //= 2

    while v > 1:
        vs.append(v)
        v //= 2

    us.reverse()
    vs.reverse()

    ind = 0
    while ind < len(us) and ind < len(vs) and vs[ind] == us[ind]:
        ind += 1

    tot = 0
    for i in range(ind, len(us)):
        tot += fee[us[i]]
    for i in range(ind, len(vs)):
        tot += fee[vs[i]]

    return tot


for q in qs:
    if q[0] == 1:
        start, end, w = max(q[1], q[2]), min(q[1], q[2]), q[3]
        weight(start, end, w)

    else:
        tot = 0
        start, end = max(q[1], q[2]), min(q[1], q[2])
        print(move(start, end))
