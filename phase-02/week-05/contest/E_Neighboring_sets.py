t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))

    left = 0
    triples = 0

    for right in range(n):
        num = a[right]
        while num - a[left] > 2:
            left += 1

        win_size = right - left + 1            
        if win_size >= 3:
            triples += (win_size - 2)*(win_size - 1)//2

    print(triples)
