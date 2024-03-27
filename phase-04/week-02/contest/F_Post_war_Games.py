for _ in range(int(input())):
    n, k = map(int, input().split())
    if n == k:
        print(0)
        continue

    res = (n - (k + 1))*3 + ((k - 1)//2)*3 + (k - 1)%2 + 1
    
    print(res)