"""

https://codeforces.com/gym/494181/problem/C

PASSED
"""

t = int(input())

for _ in range(t):
    mat, ans, curr = [], 0, 0
    m, n = map(int, input().split())

    for _ in range(m):
        row = list(map(int, input().split())
        mat.append(row)

    for i in range(m):
        for j in range(n):
            curr = mat[i][j]
            a, b = i, j

            while a < m-1 and b < n-1:
                a += 1
                b += 1
                curr += mat[a][b]
                
            a, b = i, j

            while a > 0 and b > 0:
                a -= 1
                b -= 1
                curr += mat[a][b]
                
            a, b = i, j

            while a > 0 and b < n-1:
                a -= 1
                b += 1
                curr += mat[a][b]
                
            a, b = i, j
            
            while a < m-1 and b > 0:
                a += 1
                b -= 1
                curr += mat[a][b]
                
           
            ans = max(ans, curr)

    print(ans)

    
