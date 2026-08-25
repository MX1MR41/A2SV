from collections import defaultdict


n, k = list(map(int, input().split()))
res = [0,0]
arr = list(map(int, input().split()))

cnt = defaultdict(int)
l = 0

for r in range(n):
    num = arr[r]
    cnt[num] += 1

    while len(cnt) > k:
        left = arr[l]
        cnt[left] -= 1
        if cnt[left] == 0:
            del cnt[left]

        l += 1

    if r - l > res[1] - res[0]:
        res = [l, r]

print(res[0] + 1, res[1] + 1)
