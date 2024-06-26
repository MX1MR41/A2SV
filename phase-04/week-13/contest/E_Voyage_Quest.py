import sys

x_1, y_1 = map(int, sys.stdin.readline().strip().split())
x_2, y_2 = map(int, sys.stdin.readline().strip().split())
n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

def find(ch):

    if ch == "U": return [0, 1]
    
    if ch == "D": return [0, -1]
    
    if ch == "L": return [-1, 0]
    
    if ch == "R": return [1, 0]
    
def checker(k):
        
    x_3, y_3 = x_1, y_1
    full_cycles = k // n
    extra_days = k % n

    for ch in s:
        x_3 += find(ch)[0] * full_cycles
        y_3 += find(ch)[1] * full_cycles
    
    for i in range(extra_days):
        x_3 += find(s[i])[0]
        y_3 += find(s[i])[1]
        
    return abs(x_2 - x_3) + abs(y_2 - y_3) <= k

low = 1
high = 10**15

while low <= high:

    mid = (low + high) // 2

    if checker(mid):
        high = mid - 1
    else:
        low = mid + 1

if low > 10**15:
    print(-1)
else:
    print(low)