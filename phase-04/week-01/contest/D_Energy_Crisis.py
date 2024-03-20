n, k = map(int, input().split())
arr = list(map(int, input().split()))

def chekcker(x):
    gain = 0
    need = 0
    for num in arr:
        if num > x:
            diff = num - x
            gain += (diff - diff * k / 100)
        if num < x:
            need  += (x - num)
    
    return gain >= need

low = min(arr)
high = max(arr)
while high  - low > 10 ** -7:
    mid = (high + low) / 2
    if chekcker(mid):
        low = mid
    else:
        high = mid
print(high)