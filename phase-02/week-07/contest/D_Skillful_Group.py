n = int(input())
arr = list(map(int, input().split()))

min_segment = float('inf')
l_seen = set()
arr.append(0) 

for l in range(n):

    curr = arr[l]
    r_seen = set()

    for r in range(n, l - 1, -1):
        if arr[r] in l_seen or arr[r] in r_seen:
            break

        r_seen.add(arr[r])
        min_segment = min(min_segment, r - l)
    
    if curr in l_seen:
        break

    l_seen.add(curr)
    

print(min_segment)