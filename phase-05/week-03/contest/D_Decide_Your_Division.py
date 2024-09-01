from collections import deque
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(0)
        continue

    twos = threes = fives = 0

    while not n % 2 :
        n //= 2
        twos += 1

    while not n % 3:
        n //= 3
        threes += 1

    while not n % 5:
        n //= 5
        fives += 1




    if n == 1:
        print(twos + 2 * threes + 3 * fives)
    else:
        print(-1)