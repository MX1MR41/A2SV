"""

https://codeforces.com/gym/515998/problem/F
"""

import sys
from math import gcd

def solve():
    
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    a = list(map(int, sys.stdin.readline().split()))

    lcm = 1
    vis = [0] * n
    for i in range(n):
        if vis[i]:
            continue
        cur = []
        ind = i
        
        while not vis[ind]:
            cur.append(s[ind])
            vis[ind] = 1
            ind = a[ind] - 1
        
        search = "".join(cur + cur)
        
        search = search[1:]  
        
        index = search.find("".join(cur)) + 1  
        lcm = (lcm * index) // gcd(lcm, index)
    return lcm

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        
        result = solve()
        print(result)
