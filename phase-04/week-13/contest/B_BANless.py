
for _ in range(int(input())):
    n = int(input())
    k = []
    
    start, end = 1, 3 * n 
    while start < end:
        k.append([start, end])
        start += 3
        end -= 3    

    print(len(k))
    for each in k:
        print(*each)