

for _ in range(int(input())):
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    if a == b:
        print(0)
        continue
    if abs(a - b) >= x:
        print(1)
        continue
    if r - max(a, b) >= x or min(a, b) - l >= x:
        print(2)
        continue
    if r - b >= x and a - l >= x or r - a >= x and b - l >= x:
        print(3)
        continue
    print(-1)