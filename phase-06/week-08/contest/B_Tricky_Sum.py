"""

PASSED

"""

def tot(x):
    return x*(x+1)//2

twos = []
for i in range(30):
    twos.append(2**i)


for i in range(1, 30):
    twos[i] += twos[i - 1]

# print(twos)

for _ in range(int(input())):
    n = int(input())
    ans = tot(n)
    l, r = 0, 29
    two = 0
    while l <= r:
        mid = (l + r)//2
        if 2**mid <= n:
            two = mid
            l = mid + 1
        else:
            r = mid - 1

    ans -= 2*twos[two]

    print(ans)