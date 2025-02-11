from collections import defaultdict

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    rem = defaultdict(set)

    for _ in range(m):
        u, v = list(map(int, input().split()))
        rem[v].add(u)

    arr = [i for i in range(1, n + 1)]
    for i in range(n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] in rem[key]:

            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    print(*arr)
