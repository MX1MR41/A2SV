for _ in range(int(input())):
    n = int(input().strip())
    s =  input().strip()

    pref = [1] * n
    for i in range(1, n):
        if s[i] != s[i - 1]:
            pref[i] = pref[i -1] + 1

    suff = [1] * n
    for i in range(n -2, -1, -1):
        if s[i] != s[i + 1]:
            suff[i] = suff[i + 1] + 1

    ans = [1]* (n + 1)
    if s[0] == "R":
        ans[0] += suff[0]

    for i in range(1, n):
        if s[i] == "R":
            ans[i] += suff[i]
        if s[i - 1] == "L":
            ans[i] += pref[i - 1]

    if s[-1] == "L":
        ans[-1] += pref[-1]
        
    print(*ans)
