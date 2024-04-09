def smallGCD(n, nums):
    nums.sort()
    end, cnt, last = 10 ** 5 + 1, [0] * (10 ** 5 + 1), [-1] * (10 ** 5 + 1)

    for i in range(n):
        num = nums[i]
        cnt[num] += 1
        last[num] = i

    gcd = [0] * end
    for g in range(1, end):
        small = 0
        for mid in range(g, end, g):
            if not cnt[mid]:
                continue
            cur = cnt[mid]
            cur2 = cur * (cur - 1) // 2
            cur3 = cur * (cur - 1) * (cur - 2) // 6
            bigger = n - last[mid] - 1
            gcd[g] += small * bigger * cur + small * cur2 + bigger * cur2 + cur3
            small += cur

    for g in range(end - 1, 0, -1):
        for gg in range(2 * g, end, g):
            gcd[g] -= gcd[gg]

    res = sum(gcd[i] * i for i in range(end))
    return res


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    result = smallGCD(n ,arr)
    print(result)

