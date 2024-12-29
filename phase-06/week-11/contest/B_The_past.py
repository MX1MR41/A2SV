"""

PASSED

"""

m, n = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()

seen = set(a)
for i in range(m):
    if a[i] == 0:
        while b and b[-1] in seen:
            b.pop()

        if not b:
            break

        a[i] = b.pop()

# print(a)

found = False
zero = False
for i in range(m - 1):
    if a[i] > a[i + 1]:
        found = True

    if a[i] == 0:
        zero = True

if zero or not found:
    print("No")

else:
    print("Yes")