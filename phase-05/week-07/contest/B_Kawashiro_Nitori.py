for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()

    if n < 2 * k + 1:
        print("NO")
        continue

    if k == 0:
        print("YES")
        continue

    if s[:k] == s[-k:][::-1]:
        print("YES")
    else:
        print("NO")
