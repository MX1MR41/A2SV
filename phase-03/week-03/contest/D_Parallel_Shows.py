"""

https://codeforces.com/gym/506437/problem/D

PASSED
"""

tv1, tv2 = [], []
shows = []
for _ in range(int(input())):
    shows.append(list(map(int, input().split())))


shows.sort()
for show in shows:
    if not tv1:
        tv1.append(show)
        continue

    if not tv2:
        tv2.append(show)
        continue

    if show[0] <= tv1[-1][-1]:
        if show[0] <= tv2[-1][-1]:
            print("NO")
            break
        else:
            tv2.pop()
            tv2.append(show)
    else:
        tv1.pop() 
        tv1.append(show)

else: 
    if len(tv1) > 1 or len(tv2) > 1:
        print("NO")
    else:
        print("YES")