"""

https://codeforces.com/gym/523525/problem/A

PASSED
"""

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def dfs(n, ind, path):
        # print(n, ind, path)
        if ind == n + 1: return path

        ans = None
        for i in range(1,n+1):
            if i != ind and i not in path:
                path.append(i)
                # print("CURR", ind, i , path)
                ans = dfs(n, ind + 1, path)
                if ans: return ans
                path.pop()
                
        return ans
                
            
        


        



    for _ in range(int(input())):
        n = int(input())
        for i in range(1, n+1):
            res = dfs(n, i, [])
            if res:
                print(*res)
                break

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

