from collections import defaultdict

import sys, threading

input = lambda: sys.stdin.readline().strip()



def main():

    def dfs(node, RES):
        W = B = 0
        if cols[node-1] == "B": B += 1
        else: W += 1

        neis = g[node]
        
        for nei in neis:
            temp = dfs(nei, RES)

            W += temp[0]
            B += temp[1]
            RES = max(RES, temp[2])

        if W == B: RES += 1

        return [W, B, RES]
    
    
    for _ in range(int(input())):
        n = int(input())
        verts = list(map(int, input().split()))
        cols = input()
        g = defaultdict(list)

        for i in range(n-1):
            g[verts[i]].append(i+2)


        ans = dfs(1, 0)
        print(ans[2])
    
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()





