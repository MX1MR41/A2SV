t = int(input())
skills = sorted(map(int, input().split()))
n = len(skills)

maxNum = 0
end = 0

for start in range(t):

    while end < n and skills[end] - skills[start] <= 5:
        end += 1
    maxNum = max(maxNum, end - start)

print(maxNum)