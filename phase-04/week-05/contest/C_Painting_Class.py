"""

https://codeforces.com/gym/517685/problem/C

PASSED
"""

from collections import defaultdict

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    g = defaultdict(list)

    edges = list(map(int, input().split()))

    cols = list(map(int, input().split()))

    for i in range(n-1):
        g[i+2].append(edges[i])
        g[edges[i]].append(i+2)

    def dfs(node, col, visited):
        if node in visited: return 0
        visited.add(node)

        curr = 0
        if cols[node-1] != col: 
            curr += 1
            col = cols[node-1]

        for nei in g[node]:
            curr += dfs(nei, col, visited)

        return curr

    print(dfs(1, 0, set()))
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


