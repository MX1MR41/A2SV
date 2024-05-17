"""

https://codeforces.com/gym/520390/problem/B

"""

from heapq import heappop, heappush
from collections import defaultdict

def main():
    n, k, q = map(int, input().split())
    friendship = list(map(int, input().split()))
    hashMap = defaultdict(int)
    heap = []

    for _ in range(q):
        type, friend = map(int, input().split())
        if type == 1:
            hashMap[friend] = 2
            heappush(heap, (friendship[friend - 1], friend))
        else:
            if hashMap[friend]:
                while len(heap) > k:
                    weight, f = heappop(heap)
                    hashMap[f] = 1 
            if hashMap[friend] == 2:
                print('YES') 
            else:
                print('NO')
    
if __name__ == '__main__':
    main()
 
 
