for _ in range(int(input())):
    s = input()
    n = len(s)
    ans = 0
    i = 0
    while i < n:
        if s[i] == "w":
            ans += 1
        else:
            if i > 0 and s[i-1] == "v":
                ans += 1
                if i < n-1 and s[i+1] == "v":
                    i += 1

        i += 1

    print(ans)
