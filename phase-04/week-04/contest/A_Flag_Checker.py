"""
https://codeforces.com/gym/515998/problem/A

PASSED
"""

m , n = list(map(int, input().split()))
flag = False
a = []
inbound = lambda r, c : 0 <= r < m and 0 <= c < n
for _ in range(m):
    row = list(map(int,input()))
    # print(set(row))
    if len(set(row)) > 1: flag = True
    

    a.append(row) 

if flag: 
    
    print("NO")
    exit()

def bi(r, c, col):
    if not inbound(r,c): return True

    if a[r][c] == col:
        # print("r",r,"c",c,"color",a[r][c],"col",col) 
        return False

    return bi(r+1,c,a[r][c])

for i in range(n):
    # col = a[0][i]
    curr = bi(0,i,-1)
    if not curr:
        print("NO")
        exit()

print("YES")