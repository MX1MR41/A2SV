"""

https://codeforces.com/gym/517685/problem/B

PASSED
"""

from collections import defaultdict

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    g = defaultdict(list)

    for _ in range(n-1):
        u, v, c = list(map(int, input().split()))
        g[u].append((v,c))
        g[v].append((u,c))

    def dfs(node, visited, path):
        if node in visited: return 0
        # curr = path


        visited.add(node)
        neis = g[node]
        _max = 0
        for nei, dist in neis:
            if nei not in visited:
                _max = max(_max, dfs(nei, visited, dist))

        # print("currently:", node, _max)
        return path + _max

    print(dfs(0,set(), 0))

    
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


