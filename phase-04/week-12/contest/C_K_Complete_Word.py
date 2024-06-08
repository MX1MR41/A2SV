"""

https://codeforces.com/gym/527294/problem/C

"""

from collections import defaultdict, Counter


for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    
    freq = defaultdict(Counter)
    for i in range(n):
        loc = min(i % k, k - i % k - 1)
        freq[loc][s[i]] += 1
    
    changes_needed = 0
    tot = 2 * (n // k)
    for i in range(k // 2):
        max_freq= max(freq[i].values())
        changes_needed += tot - max_freq
    
    if k % 2:
        max_freq = max(freq[k//2].values())
        changes_needed += n//k - max_freq
    
    print(changes_needed)
