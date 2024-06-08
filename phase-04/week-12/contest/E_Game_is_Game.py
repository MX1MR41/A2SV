"""

https://codeforces.com/gym/527294/problem/E

"""

import sys, threading
from sys import stdin

def input(): return stdin.readline().strip()

def main():
    N, K = map(int, input().split())

    root = {}

    def add(s):
        cur = root
        for ch in s:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]

    for _ in range(N):
        s = input()
        add(s)

    def get_winner(node): 
        can_win = False
        can_lose = False
        for ch in node:
            result = get_winner(node[ch])
            if result == 1:
                can_win = True
            elif result == -1:
                can_lose = True
            else:
                can_win = can_lose = True

        if can_win == False: 
            return 1
        elif can_lose == False: 
            return -1
        else:
            return 0

    first_can_win = False
    first_can_lose = False
    for ch in root:
        result = get_winner(root[ch])
        if result == 1:
            first_can_win = True
        elif result == -1:
            first_can_lose = True

    if first_can_win and (K%2 or first_can_lose):
        print("First")
    else:
        print("Second")

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()