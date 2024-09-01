for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    def is_valid_waiting_time(waiting_time):
        start = nums[0]
        count = 1

        for i in range(1, n):
            if (nums[i] - start + 1) // 2 > waiting_time:
                count += 1
                start = nums[i]

        return count <= 3

    l = 0
    r = max(nums)

    while l <= r:
        mid = (l + r) // 2
        if is_valid_waiting_time(mid):
            r = mid - 1
        else:
            l = mid + 1

    print(l)
