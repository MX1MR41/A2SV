from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ave = sum(arr)/n


    target = sum(arr) - (ave * (n-2))

    seen = defaultdict(int)

    ans = 0
    for i in arr:
        j = target - i
        ans += seen[j]
        seen[i] += 1

    print(ans)



        



