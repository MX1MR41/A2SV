from math import ceil

for t in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    powers = list(map(int, input().split()))

    stk = [(float("inf"), powers[0])]
    res = 0
    for i in range(1, n):
        time = 0
        while h[i] - (stk[-1][0] - time) * stk[-1][-1] > 0:
            t, p = stk.pop()
            h[i] -= (t - time) * p
            time += (t - time)
       
        time += ceil(h[i] / stk[-1][-1])
        stk.append((time, powers[i]))
        res = max(res, time)
   
    print(res)
