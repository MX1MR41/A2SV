"""
https://codeforces.com/contest/1676/problem/F

"""

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    nums.sort()

    arr = []
    prev = [0, 0]

    for i in range(len(nums)):
        num = nums[i]
        if arr and arr[-1] == num:
            continue

        if num == prev[0]:
            prev[1] += 1
            if prev[1] >= k:
                arr.append(num)
                prev[1] = float("-inf")
        else:
            prev = [num, 1]
            if k == 1:
                arr.append(num)
                prev[1] = float("-inf")


    left = 0
    res = [0, 0, 0]

    for right in range(len(arr)):
        if arr[right] - arr[left] != right - left:
            left = right

        curr = right - left + 1
        if curr > res[0]:
            res = [curr, arr[left], arr[right]]

    if res[0] == 0:
        print(-1)
    else:
        print(*res[1:])
