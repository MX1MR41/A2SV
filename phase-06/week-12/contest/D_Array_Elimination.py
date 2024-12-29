"""

PASSED

"""


from collections import defaultdict


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    count = defaultdict(int)
    for a in arr:
        l = len(bin(a)[2:])
        need = 31 - l
        x = "0"*need + bin(a)[2:]
        for i in range(31):
            if x[i] == "1":
                count[i] += 1

    
        # print(x)

    res = []
    for i in range(1, n + 1):
        possible = True
        for x, j in count.items():
            if j % i:
                possible = False
                break

        if possible:
            res.append(i)

    print(*res)



    # print("*"*20)