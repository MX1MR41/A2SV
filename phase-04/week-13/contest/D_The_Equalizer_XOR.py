import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    pref_xor = [a[0]]
    for i in range(1, n):
        pref_xor.append(pref_xor[-1] ^ a[i])
    
    
    suf_xor = 0
    last_idx = defaultdict(lambda : -1) 

    for i in range(n - 1, -1, -1):
        suf_xor ^= a[i]
        last_idx[suf_xor] = max(last_idx[suf_xor], i)
    
    yes = False
 
    for i in range(n):
        # two subarrays
        first = pref_xor[i]
        second = pref_xor[-1] ^ first
        if first == second:
            yes = True
            break
        
        # three subarrys
        # the prefix xor should occur as a sufix after this index 
        if pref_xor[-1] ^ first == 0 and last_idx[first] > i:
            yes = True
            break

    print('YES' if yes else 'NO')