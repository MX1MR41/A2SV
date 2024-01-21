"""

https://codeforces.com/gym/497696/problem/A

PASSED
"""

t = int(input())

for  _ in range(t):
    n = int(input())
    arr1 = input()
    arr2 = input()
    i, j = 0, 0

    while i < n:
        a , b = arr1[i], arr2[j]
        if (a == "R" and b != "R") or (b == "R" and a != "R"):
            print("NO")
            break
        if ((a == "B" or a =="G") and b == "R") or ((b == "B" or b =="G") and a == "R"):
            print("NO")
            break

        i += 1
        j += 1

    else:
        print("YES")
