"""

https://codeforces.com/gym/570406/problem/A

PASSED

"""

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    i = 0

    while i < n - 1:
        if arr[i] % 2 == arr[i + 1] % 2:
            j = i + 1
            while j < n and arr[i] % 2 == arr[j] % 2:
                ans += 1
                j += 1

            i = j
        else:
            i += 1


    print(ans)

            
