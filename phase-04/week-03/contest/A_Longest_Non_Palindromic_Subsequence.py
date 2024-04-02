"""

https://codeforces.com/gym/514644/problem/A


PASSED

"""

for _ in range(int(input())):
    s = input()
    SET = set(s)
    if len(SET) <= 1:
        print(-1)
        continue

    print(len(s) - 1)