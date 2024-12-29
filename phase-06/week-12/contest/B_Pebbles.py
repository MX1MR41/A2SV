"""

PASSED

"""

n = int(input())

count = n
while n:
    div = 1
    for i in range(2, n):
        if not n % i:
            div = i
            break

    if div == 1:
        count += 1
        break

    cols = n//div
    count += cols
    n = cols


print(count)

