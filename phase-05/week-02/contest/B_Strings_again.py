"""


PASSED
"""

for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))
    a = sorted(list(input()), reverse=True)
    b = sorted(list(input()), reverse=True)

    c = []

    cnt = 0
    last = None
    while a and b:
        if cnt == k:
            if last == "a":
                c.append(b.pop())
                last = "b"
                cnt = 1
            else:
                c.append(a.pop())
                last = "a"
                cnt = 1
        else:

            if a[-1] < b[-1]:
                c.append(a.pop())
                if last == "a":
                    cnt += 1
                else:
                    cnt = 1
                last = "a"

                if not a or not b:
                    break

            else:
                c.append(b.pop())
                if last == "b":
                    cnt += 1
                else:
                    cnt = 1
                last = "b"

                if not a or not b:
                    break

    print("".join(c))
