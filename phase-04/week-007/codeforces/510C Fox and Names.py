from collections import defaultdict

import sys, threading

input = lambda: sys.stdin.readline().strip()


def main():
    words = []
    g = defaultdict(list)
    n = int(input())
    for _ in range(n):
        words.append(input())

    # adjacent comparison of words suffices instead of quadratic
    # since the words are supposedly "sorted"
    for i in range(n - 1):
        prev, nxt = words[i], words[i + 1]
        lenp, lenn = len(prev), len(nxt)
        for j in range(min(lenp, lenn)):
            if prev[j] != nxt[j]:

                g[prev[j]].append(nxt[j])
                break
        
        # an edge case: if there exists two strings xy and x such that xy < x
        if lenp > lenn and nxt in prev[:lenn]:
            print("Impossible")
            exit()

    order = []

    cols = defaultdict(int)

    # topological sort using dfs
    def dfs(node, cols):
        if cols[node] == 1:
            return

        cols[node] = -1
        neis = g[node]

        for nei in neis:
            if cols[nei] == -1:
                print("Impossible")
                exit()
            if cols[nei] == 0:
                dfs(nei, cols)

        cols[node] = 1

        order.append(node)

    for i in [chr(i) for i in range(97, 123)]:
        dfs(i, cols)

    print("".join(order[::-1]))


if __name__ == "__main__":

    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
