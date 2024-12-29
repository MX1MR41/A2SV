"""

PASSED

"""

for _ in range(int(input())):
    n, k, z = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    score = arr[0]
    arr = arr[:k + 1]

    ans = sum(arr)
    # print(ans)
    # print("final arr", arr)

    n = len(arr)
    m = 0
    pre = 0
    for i in range(n):
        j = i + 1
        if j < n:
            m = max(m, arr[i] + arr[j])
        pre += arr[i]  

    
        moves = (k - i) // 2
        if moves <= z:
            ans = max(ans, pre + m * moves)

    print(ans)



