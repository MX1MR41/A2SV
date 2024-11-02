"""

PASSED

"""

for _ in range(int(input())):
    caves = int(input())
    arr = []
    for _ in range(caves):
        temp = list(map(int, input().split()))
        n = temp[0]
        temp = temp[1:]
        need = 0
        for i in range(n):
            x = temp[i]
            need = max(need, x- i + 1)

        arr.append((need, need + n))

    arr.sort()
    # print(arr)
    ans = arr[0][0]
    last = arr[0][1]
    for need, get in arr[1:]:
        diff = max(0, need - last)
        gain = get - need
        ans += diff
        last += diff + gain


    print(ans)