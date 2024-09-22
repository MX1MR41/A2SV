from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    uni = list(map(int, input().split()))
    skills = list(map(int, input().split()))

    uni_students = defaultdict(list)
    for i in range(n):
        uni_students[uni[i]].append(skills[i])

    for uni in uni_students:
        uni_students[uni].sort(reverse=True)

    ans = [0] * (n + 1)

    for uni in uni_students:
        students = uni_students[uni]
        m = len(students)

        prefix_sum = [0] * (m + 1)
        for i in range(m):
            prefix_sum[i + 1] = prefix_sum[i] + students[i]

        for k in range(1, m + 1):
            teams = m // k
            if teams > 0:
                ans[k] += prefix_sum[teams * k]

    print(*ans[1 : n + 1])
