"""

https://codeforces.com/gym/503628/problem/B

PASSED
"""
s = input()
m = int(input())
queries = []

for _ in range(m):
    queries.append(list(map(int, input().split())))

pref = [0]
for indx in range(len(s) - 1):
    if s[indx] == s[indx + 1]:
        pref.append(pref[-1] + 1)
    
    else:
        pref.append(pref[-1])


for left, right in queries:
    print(pref[right - 1] - pref[left - 1])