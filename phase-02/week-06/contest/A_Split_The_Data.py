"""

https://codeforces.com/gym/500982/problem/A

PASSED
"""

n = int(input())
usb = []
m = int(input())
m2 = 0
res = 0

for _ in range(n):
    usb.append(int(input()))


usb.sort(reverse = True)

for i in usb:
    if m2 >= m:
        print(res)
        break

    res += 1
    m2 += i

else:
    print(res)
