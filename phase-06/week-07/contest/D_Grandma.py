"""


PASSED

"""

for _ in range(int(input())):
    n = int(input())
    s = input()
    if s == s[::-1] or n == 1:
        print(0)
        continue

    letters = set(list(s))
    res = float("inf")
    for letter in letters:
        l, r = 0, n - 1
        count = 0
        possible = True
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                count += 1
                if s[l] == letter:
                    l += 1
                elif s[r] == letter:
                    r -= 1
                else:
                    possible = False
                    break
        if possible:
            res = min(res, count)

    print(res) if res != float("inf") else print(-1)

        



    