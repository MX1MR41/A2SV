"""

https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

"""

from collections import deque


n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

min_que = deque()
max_que = deque()
res = 0
left = 0
for right in range(n):
    curr = arr[right]
    while min_que and min_que[-1][0] > curr:
        min_que.pop()

    min_que.append((curr, right))

    while max_que and max_que[-1][0] < curr:
        max_que.pop()

    max_que.append((curr, right))

    while min_que and max_que and max_que[0][0] - min_que[0][0] > k:
        
        left += 1
        while min_que and min_que[0][1] < left:
            min_que.popleft()

        while max_que and max_que[0][1] < left:
            max_que.popleft()

    res += right - left + 1

print(res)
