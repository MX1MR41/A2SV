"""

https://codeforces.com/contest/1385/problem/D

"""

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def dfs(l, r, x, s):

        if l == r:
            return 0 if s[l] == x else 1
        
        mid = (l + r)//2 + 1
        

        left = mid - l - s[l:mid].count(x)
        first = left + dfs(mid, r, chr(ord(x) + 1), s)

        right = r - mid + 1 - s[mid:r + 1].count(x)
        second = right + dfs(l, mid - 1, chr(ord(x) + 1), s)

        return min(first, second)

    for _ in range(int(input())):
        n = int(input())
        s = input()

        if n == 1:
            if s == 'a':
                print(0)
            else:
                print(1)

            continue

        mid = n//2
        
        left = mid - s[:mid].count('a')
        
        
        first = left + dfs(mid, n - 1, chr(ord('a') + 1), s)

        right = n - mid - s[mid:n].count('a')
        second = right + dfs(0, mid - 1, chr(ord('a') + 1), s)

        print(min(first, second))


if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

