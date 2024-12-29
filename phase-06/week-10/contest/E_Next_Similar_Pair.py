from collections import defaultdict, deque
import sys

sys.setrecursionlimit(300000)

def dfs_iterative(root, a, g, cnt, ans):
    stack = [(root, -1)]
    post_order = []
    while stack:
        node, parent = stack.pop()
        post_order.append((node, parent))
        for neighbor in g[node]:
            if neighbor != parent:
                stack.append((neighbor, node))

    for v, parent in reversed(post_order):
        best_child = -1
        for u in g[v]:
            if u != parent:
                if best_child == -1 or len(cnt[best_child]) < len(cnt[u]):
                    best_child = u

        if best_child != -1:
            cnt[v], cnt[best_child] = cnt[best_child], cnt[v]

        for u in g[v]:
            if u != parent and u != best_child:
                for color, count in cnt[u].items():
                    if color != a[v]:
                        ans[0] += cnt[v].get(color, 0) * count
                    cnt[v][color] = cnt[v].get(color, 0) + count

        ans[0] += cnt[v].get(a[v], 0)
        cnt[v][a[v]] = 1


def solve():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n

        g = [[] for _ in range(n)]
        for _ in range(n - 1):
            v, u = map(int, data[idx:idx + 2])
            idx += 2
            v -= 1
            u -= 1
            g[v].append(u)
            g[u].append(v)

        cnt = [defaultdict(int) for _ in range(n)]
        ans = [0]
        dfs_iterative(0, a, g, cnt, ans)
        results.append(ans[0])

    sys.stdout.write("\n".join(map(str, results)) + "\n")


if __name__ == "__main__":
    solve()
