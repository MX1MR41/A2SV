for _ in range(int(input())):
    n, q = list(map(int , input().split()))
    arr = []
    for _ in range(n):
        b, x = list(map(int, input().split()))
        if b == 1: arr.append(x)
        else:
            arr += arr * x

    qs = list(map(int, input().split()))

    ans = []
    for q in qs:
        ans.append(arr[q - 1])

    print(*ans)