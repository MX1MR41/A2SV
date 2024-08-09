for _ in range(int(input())):
    a, b, c, n = map(int, input().split())
    n -= 3 * max(a, b, c) - a - b - c
    print('YES' if n % 3 == 0 and n >= 0 else 'NO')