from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

cnt = Counter(arr)
res = 0

while len(cnt) > 0:
    res += (len(cnt) - 1)
    keys = list(cnt.keys())

    for key in keys:
        cnt[key] -= 1

        if cnt[key] == 0:
            del cnt[key]

print(res)