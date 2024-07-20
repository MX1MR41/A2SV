from collections import defaultdict

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def dfs(v, child, respect, ans):
        ok = respect[v]
        for ch in child[v]:
            if respect[ch] == 0:
                ok = False
            dfs(ch, child, respect, ans)
        if ok:
            ans.append(v + 1)

    N = int(input())

    child = defaultdict(list)
    respect = [0]*N

    root = 0

    for ch in range(N):
        p, c = map(int, input().split())
        p -= 1
        respect[ch] = c
        if p == -2:
            root = ch
            continue
        child[p].append(ch)

    ans = []

    dfs(root, child, respect, ans)

    if not ans:
        print(-1)
    else:
        print(*sorted(ans))

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


