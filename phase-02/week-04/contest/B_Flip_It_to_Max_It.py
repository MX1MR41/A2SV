"""

https://codeforces.com/gym/497696/problem/B

PASSED
"""

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    tot = sum(abs(num) for num in nums)
    op = 0


    l  = r = 0

    while l < n and nums[l] >= 0 :
        l += 1
        r += 1

    while r < n:
        if nums[r] <= 0:
            while r < n and nums[r] <= 0:
                r += 1
            op += 1
        else:
            while r < n and nums[r] >= 0:
                r += 1

            l = r


    print(tot, op)

        