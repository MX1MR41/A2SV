"""

https://codeforces.com/edu/course/2/lesson/9/3/practice/contest/307094/problem/D

"""

ncaps = int(input())
caps = list(map(int, input().split()))
nshirts = int(input())
shirts = list(map(int, input().split()))
npants = int(input())
pants = list(map(int, input().split()))
nshoes = int(input())
shoes = list(map(int, input().split()))

caps.sort()
shirts.sort()
pants.sort()
shoes.sort()

caps.append(float("inf"))
shirts.append(float("inf"))
pants.append(float("inf"))
shoes.append(float("inf"))

res = [float("inf")]*5

# print(caps)
# print(shirts)
# print(pants)
# print(shoes)

a = b = c = d = 0



while a < ncaps and b < nshirts and c < npants and d < nshoes:
    if caps[a] == shirts[b] == pants[c] == shoes[d] == float("inf"):
        break

    # curr = caps[a] + shirts[b] + pants[c] + shoes[d]
    m = min(caps[a], shirts[b], pants[c], shoes[d])
    M = max(caps[a], shirts[b], pants[c], shoes[d])
    curr = M - m

    if curr < res[0]:
        res = [curr, caps[a], shirts[b], pants[c], shoes[d]]

    # print(caps[a], shirts[b], pants[c], shoes[d])

    if caps[a] == m:
        a += 1

    if shirts[b] == m:
        b += 1

    if pants[c] == m:
        c += 1

    if shoes[d] == m:
        d += 1

print(*res[1:])
