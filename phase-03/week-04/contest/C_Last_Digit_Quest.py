"""

https://codeforces.com/gym/508328/problem/C

PASSED
"""

from collections import defaultdict


for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    freq = defaultdict(int)

    for num in arr:
        freq[num % 10] += 1

    def f():
        for i in range(10):
            freq[i] -= 1
            for j in range(10):
                freq[j] -= 1
                for k in range(10):
                    freq[k] -= 1
                    if (i+j+k)%10 == 3 and freq[i] >= 0 and freq[j] >= 0 and freq[k] >= 0:
                        return "YES"
                    freq[k] += 1
                freq[j] += 1
            freq[i] += 1
                    
        return "NO"
    
    print(f())

    