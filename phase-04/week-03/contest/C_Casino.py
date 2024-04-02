N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
    while arr[i]%2 == 0:
        arr[i] //= 2
    while arr[i]%3 == 0:
        arr[i] //= 3

for i in range(1, N):
    if arr[i] != arr[i-1]:
        print("No")
        exit()

print("Yes")