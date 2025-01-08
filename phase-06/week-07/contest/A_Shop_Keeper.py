"""

https://codeforces.com/gym/568645/problem/A

PASSED

"""

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    tot = sum(arr)
    price = arr[-1]
    left, right = arr[0], arr[-1]
    while left <= right:
        mid = (left + right)//2
        if n * mid >= tot:
            price = mid
            right = mid - 1
        else:
            left = mid + 1

    print(price)