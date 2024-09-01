"""

https://codeforces.com/gym/545013/problem/B

PASSED

"""

n, a, b = list(map(int, input().split()))
arr = list(map(int, input().split()))

if a + b > n:
    print(0)
    exit()

arr.sort()
seen = set()
freqs = []
freq = 0
for i in arr:
    if i not in seen:
        seen.add(i)
        freq += 1

    freqs.append(freq)

# print(freqs)

ans = freqs[b] - freqs[b - 1]
# print("ans", ans)
if not ans:
    print(0)
else:
    print(arr[b] - arr[b-1])