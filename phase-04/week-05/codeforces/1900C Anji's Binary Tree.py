from collections import defaultdict

def dfs_iterative(start, s, left, right):
    stack = [(start, 0)]  # (node, current count)
    min_count = float('inf')

    while stack:
        node, curr = stack.pop()
        lc, rc = left[node], right[node]

        if not lc and not rc:
            min_count = min(min_count, curr)
        else:
            if s[node-1] == "U":
                if lc: stack.append((lc, curr + 1))
                if rc: stack.append((rc, curr + 1))
            elif s[node-1] == "R":
                if lc: stack.append((lc, curr + 1))
                if rc: stack.append((rc, curr))
            elif s[node-1] == "L":
                if lc: stack.append((lc, curr))
                if rc: stack.append((rc, curr + 1))

    return min_count

for _ in range(int(input())):
    n = int(input())
    s = input()
    left, right = defaultdict(int), defaultdict(int)

    for i in range(n):
        l, r = map(int, input().split())
        if l: left[i+1] = l 
        if r: right[i+1] = r

    res = dfs_iterative(1, s, left, right)
    print(res)
