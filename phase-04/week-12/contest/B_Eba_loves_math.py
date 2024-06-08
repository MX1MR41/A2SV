"""

https://codeforces.com/gym/527294/problem/B

"""



for _ in range(int(input())):

    n = int(input())

    nums = list(map(int, input().split()))

    x = nums[0]

    for i in range(1, n):

        x &= nums[i]
        
    print(x)