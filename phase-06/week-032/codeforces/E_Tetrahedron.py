# https://codeforces.com/problemset/problem/166/E
# matrix exponentiation

MOD = 10**9 + 7

def multiply(mat1, mat2):
    rows = len(mat1)
    cols = len(mat2[0])
    res = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        row = mat1[r]
        for c in range(cols):
            col = [mat2[i][c] for i in range(rows)]

            cell = 0 

            for k in range(rows):
                cell = (cell + (row[k] * col[k])) % MOD 

            res[r][c] = cell

    return res

def power(mat, exponent):
    if exponent == 1:
        return mat
    
    half = power(mat, exponent//2)
    res = multiply(half, half)
    if exponent % 2:
        res = multiply(mat, res)

    return res


mat = [
    [0,1,1,1],
    [1,0,1,1],
    [1,1,0,1],
    [1,1,1,0]
]

n = int(input())
res = power(mat, n)
print(res[-1][-1])

