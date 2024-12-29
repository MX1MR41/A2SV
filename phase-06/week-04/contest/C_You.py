
ans = [-1] * 16
ans[0] = 0

for i in range(1, 16):
    for j in [4, 6, 9]:  
        if i >= j and ans[i - j] != -1:
            ans[i] = max(ans[i], ans[i - j] + 1)


q = int(input())
for _ in range(q):
    n = int(input())
    if n < 16:
        print(ans[n])
    else:
        t = (n - 16) // 4 + 1
        print(t + ans[n - 4 * t])
