from collections import deque
n , k = list(map(int,input().split()))
a = list(map(int,input().split()))
if not k or not a:
    print("")
elif len(a) == 1:
    for _ in range(k):
        print(a[0])

else:

    for _ in range(k):
        q = deque(a)
        i = int(input())
        for _ in range(i-1):
            if q[0] < q[1]:
                q.append(q.popleft())
            else:
                a, b = q.popleft(), q.popleft()
                q.appendleft(a)
                q.append(b)


        print(q[0], q[1])


