for _ in range(int(input())):
    n = int(input())
    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))

    if n == 1:
        print("YES")
        print(7)
        continue

    ans = []
    # print(n, "matrix",mat)

    for i in range(n):

        curr = []


        a = i
        b = i + 1
        while a < n and  b < n:
            curr.append(mat[a][b])
            b += 1 

        b = i
        a = i - 1
        while a >= 0 and  b >= 0:
            curr.append(mat[a][b])
            a -= 1 

        # print(i, curr)
        if not curr: break
        m = len(curr)
        x = curr.pop()
        # ans.append(x)
        for _ in range(m - 1):
            x &= curr.pop()
        # print(i, x)
        ans.append(x)

    flag = True

    for i in range(n-1):
        if not flag: break
        for j in range(i+1, n):
            if ans[i] | ans[j] != mat[i][j]:
                print("NO")
                flag = False
                break

    if flag:
        print("YES")
        print(*ans)

    # print("\n\n")


    


