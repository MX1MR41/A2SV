g = {
    1: "a", 2: "a", 3: "a", 4: "a",
    5: "b", 6: "b", 7: "b",
    8: "c", 9: "c"
}

for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    if g[x] == g[y]:
        print("Yes")
    else:
        print("No")