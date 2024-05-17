"""

https://codeforces.com/gym/515998/problem/B


"""

from collections import defaultdict
import sys, threading

input = lambda: sys.stdin.readline().strip()


def main():

    def bus(node, pre, visited):
        if node not in visited:
            visited.add(node)
            nei = g[node]
            if len(nei) == 1:
                if nei[0] == pre:
                    return True
            curr = True
            for i in nei:
                if i != pre:
                    curr = bus(i, node, visited)
            return curr

    def ring(node, pre, visited):
        if node not in visited:
            visited.add(node)
            nei = g[node]
            if pre in nei and 1 in nei:
                return True

            curr = True
            for i in nei:
                if i != pre:
                    curr = bus(i, node, visited)
            return curr

    n, e = list(map(int, input().split()))

    g = defaultdict(list)

    for _ in range(e):
        u, v = list(map(int, input().split()))
        g[u].append(v)
        g[v].append(u)

    cnt = defaultdict(int)

    for i in g:
        cnt[len(g[i])] += 1

    nei = g[1]

    if len(cnt) == 2 and cnt[1] == 2 and cnt[2] == n - 2:
        visited = set()
        # print(cnt)
        visited.add(1)
        curr = bus(nei[0], 1, visited)
        if curr:
            print("bus topology")
            exit()

    if len(cnt) == 2 and n - 1 in cnt and 1 in cnt:
        print("star topology")
        exit()

    curr = False
    if len(cnt) == 1 and len(cnt) == 1 and 2 in cnt:
        visited = set()
        visited.add(1)
        # print(cnt)
        curr = ring(min(nei), 1, visited)
        if curr:
            print("ring topology")
            exit()

    # print(g)
    # print(cnt)
    print("unknown topology")

    # print("cnt:",cnt)

    # print(g)


if __name__ == "__main__":

    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
