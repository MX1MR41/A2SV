from heapq import heapify, heappush, heappop, heapreplace


for _ in range(int(input())):
    n = int(input())
    soc = list(map(int, input().split()))
    heap = [[-soc[i], i + 1] for i in range(n)]
    heapify(heap)

    tot, meets = 0, []
    while True:
        a = heappop(heap)
        b = heappop(heap)

        if a[0] == 0 or b[0] == 0:
            break

        a[0] += 1
        b[0] += 1

        tot += 1
        meets.append([a[1], b[1]])

        heappush(heap, a)
        heappush(heap, b)

    print(tot)
    for meet in meets:
        print(*meet)
