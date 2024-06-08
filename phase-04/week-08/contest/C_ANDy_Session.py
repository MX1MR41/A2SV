"""

https://codeforces.com/gym/522079/problem/C

"""

for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    needs = [0] * 31

    for loc in range(31):
        for num in nums:
            if num & (1 << loc) == 0:
                needs[loc] += 1
    
    max_val = 0

    for i in range(len(needs) - 1, -1, -1):
        if needs[i] <= k:
            max_val |= (1 << i)
            k -= needs[i]
    
    print(max_val)