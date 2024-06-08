"""

https://codeforces.com/gym/523525/problem/E

"""
n, k = map(int, input().split())
nums = list(map(int, input().split()))

suffix = [nums[-1]]
for i in range(n - 2, -1, -1):
    suffix.append(suffix[-1] + nums[i])

ans = suffix.pop()
suffix.sort(reverse=True)
for i in range(k - 1):
    ans += suffix[i]
print(ans)