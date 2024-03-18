from bisect import bisect_right
n = int(input())
arr = sorted(list(map(int, input().split())))
for _ in range(int(input())):
    d = int(input())
    ind = bisect_right(arr, d)

    print(ind)
