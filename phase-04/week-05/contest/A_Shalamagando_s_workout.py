"""

https://codeforces.com/gym/517685/problem/A

PASSED
"""

n = int(input())
arr = list(map(int, input().split()))

chest = biceps = back = 0

for i in range(0, n, 3):
    chest += arr[i]
    if i + 1 < n: biceps += arr[i+1]
    if i + 2 < n: back += arr[i+2]
    


if biceps < chest > back: print("chest")
elif chest < biceps > back: print("biceps")
else: print("back")