"""

https://codeforces.com/gym/545013/problem/D

PASSED

"""

summ = lambda x: x*(x+1)/2

def search(n):
    l, r = 1, 10000000000
    ans = 0

    while l <= r:
        m = (l + r)//2
        if summ(m) <= n:
            ans = m
            l = m + 1
        else:
            r = m - 1

    return ans

for _ in range(int(input())):
    n = int(input())

    a = b = 0

    turns = search(n)
    # print("n:",n, "turns",turns,"\n")
    tot = 0
    curr = 1
    flag = True

    last = ("a", "o", 1)

    for i in range(1,  turns + 1):
        if last[0] == "a":
            if last[1] == "o":
                if i % 2:
                    a += i
                    if last[-1] == 1:
                        last = ("b", "e", 0)
                    else:
                        last = ("a", "e", 1)
            else:
                if not i % 2:
                    a += i
                    if last[-1] == 1:
                        last = ("b", "o", 0)
                    else:
                        last = ("a", "o", 1)

        else:
            if last[1] == "o":
                if i % 2:
                    b += i
                    if last[-1] == 1:
                        last = ("a", "e", 0)
                    else:
                        last = ("b", "e", 1)
            else:
                if not i % 2:
                    b += i
                    if last[-1] == 1:
                        last = ("a", "o", 0)
                    else:
                        last = ("b", "o", 1)

        # print("i:", i, "a:", a, "b:", b, "last:", last)
                

    if a + b < n:
        if last[0] == "a":
            a += n - (a+b)
        else:
            b += n - (a+b)

    print(a,b,)

        
        



    # print(turns)