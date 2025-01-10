def fk(x, a, k):
    distances = [abs(x - ai) for ai in a]
    distances.sort()
    return distances[k]

t = int(input())  
results = []

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    
    l, r = a[0], a[-1]  
    best_x = l  

    while l <= r:
        mid = (l + r) // 2
        left_value = fk(mid - 1, a, k) if mid - 1 >= a[0] else float('inf')
        mid_value = fk(mid, a, k)
        right_value = fk(mid + 1, a, k) if mid + 1 <= a[-1] else float('inf')

        if mid_value <= left_value and mid_value <= right_value:
            best_x = mid
            break
        elif left_value < mid_value:
            r = mid - 1
        else:
            l = mid + 1

    results.append(best_x)

print("\n".join(map(str, results)))


