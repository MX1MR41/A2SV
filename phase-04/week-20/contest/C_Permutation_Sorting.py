
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    prev = set()
    ans = 0
    for num in nums:
        if num + 1 in prev:
            ans += 1
        prev.add(num)
        
    print(ans)
