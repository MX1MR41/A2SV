T = int(input())
for _ in range(T):
    x = int(input())
    total = 0
    prizes = [400, 300, 200, 150, 100]
    if x <= 5:
        total += prizes[x - 1]
    print(total)