t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    ans = []
    c = n - 1
    i = 0
    while i < len(nums):
     
        ans.append(nums[i])
        i += c
        c -= 1
 
    ans.append(10**9)
    print(*ans)