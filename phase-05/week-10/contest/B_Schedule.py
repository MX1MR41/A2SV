"""

PASSED

"""

n = int(input())
s = list(map(int, input().split()))

tot = 0

tot += s.count(1)

for i in range(1, n-1):
    if not s[i]:
        if s[i-1] and s[i+1]:
            tot += 1

print(tot)