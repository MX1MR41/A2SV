for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    visited = set()
    right_most = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        if arr[i] not in visited:
            visited.add(arr[i])
            right_most[i + 1] = 1
            visited.add(arr[i])
    
    for i in range(1, len(right_most)):
        right_most[i] += right_most[i - 1]

    visited.clear()
    ans = 0
    for i in range(n):
        if arr[i] not in visited:
            ans += right_most[-1] - right_most[i]
            visited.add(arr[i])

    print(ans)