"""

PASSED

"""

n, a, b = list(map(int, input().split()))
a -= 1
arr = [i for i in range(1, n + 1)]
print(arr[(a + b)%n])
