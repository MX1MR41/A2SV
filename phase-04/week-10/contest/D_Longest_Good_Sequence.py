"""

https://codeforces.com/gym/524965/problem/D

"""

import sys

n = int(sys.stdin.readline().strip())

nums = list(map(int, sys.stdin.readline().strip().split()))

if n == 1 and nums[0] == 1:
    print(1)
    sys.exit()

def find_divisors(number):
    divisors = []
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)

    return divisors  


dp = [0] *(max(nums) + 1)

for num in nums:
    divisors = find_divisors(num)
    dp[num] = 1
    for div in divisors:
        dp[num] = max(dp[num], dp[div] + 1)

    for div in divisors:
        dp[div] = max(dp[div], dp[num])
print(max(dp))