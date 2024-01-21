"""

https://codeforces.com/gym/497696/problem/D

"""


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    groups = ["RGB", "GBR", "BRG"]
    res = float('inf')

    for group in groups:
        matches = 0
        for right in range(k): 
            if group[right%3] == s[right]:
                matches += 1
        
        max_matches = matches
        for right in range(k, n):
            left = right - k
            if group[right%3] == s[right]:
                matches += 1
            if group[left%3] == s[left]:
                matches -= 1
            
            max_matches = max(matches, max_matches)
        
        res = min(res, k - max_matches)
    
    print(res)