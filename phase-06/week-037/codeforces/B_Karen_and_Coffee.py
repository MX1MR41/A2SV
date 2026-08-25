# https://codeforces.com/problemset/problem/816/B

# Solution 1 using prefix sum with array

n, k, q = list(map(int, input().split()))
rs = []
pre = [0] * (200002)
for _ in range(n):
    l, r = list(map(int, input().split()))
    pre[l] += 1
    pre[r + 1] -= 1

for i in range(1, 200002):
    pre[i] += pre[i - 1]

admissible_count_pre = []
admissible_count = 0

for i in range(200002):
    if pre[i] >= k:
        admissible_count += 1

    admissible_count_pre.append(admissible_count)

for _ in range(q):
    l, r = list(map(int, input().split()))
    count = admissible_count_pre[r] - admissible_count_pre[l - 1] if l - 1 >= 0 else admissible_count_pre[r]

    print(count)



# Solution 2 using prefix sum with hashmap
from collections import defaultdict


n, k, q = list(map(int, input().split()))
pre = defaultdict(int)
for _ in range(n):
    l, r = list(map(int, input().split()))
    pre[l] += 1
    pre[r + 1] -= 1

flattened_pre = []
prefix_sum = 0

for temp in sorted(pre.keys()):
    prefix_sum += pre[temp]
    flattened_pre.append([temp, prefix_sum])

admissible_ranges = []
for i in range(len(flattened_pre) - 1):
    temp, count = flattened_pre[i]
    if count >= k:
        next_temp = flattened_pre[i + 1][0]
        admissible_ranges.append([temp, next_temp - 1])


admissible_prefix = []
admissible_prefix_sum = 0
for l, r in admissible_ranges:
    admissible_prefix.append(admissible_prefix_sum)
    admissible_prefix_sum += r - l + 1


def find_count_at(temp):
    if not admissible_ranges or temp < admissible_ranges[0][0]:
        return 0

    l, r = 0, len(admissible_ranges) - 1
    res = 0

    while l <= r:
        mid = (l + r) // 2

        if admissible_ranges[mid][0] <= temp <= admissible_ranges[mid][1]:
            pre = admissible_prefix[mid]
            count_in_interval = temp - admissible_ranges[mid][0] + 1
            res = pre + count_in_interval
            return res

        elif temp > admissible_ranges[mid][0]:
            pre = admissible_prefix[mid]
            count_in_interval = admissible_ranges[mid][1] - admissible_ranges[mid][0] + 1
            res = pre + count_in_interval
            l = mid + 1

        else:
            r = mid - 1

    return res

for _ in range(q):
    l, r = list(map(int, input().split()))
    count = find_count_at(r) - find_count_at(l - 1)

    print(count)


