"""

https://codeforces.com/gym/526229/problem/D

"""


import sys
   
class Node:
    def __init__(self):
        self.children = [None, None]

class Trie:
    def __init__(self, val):
        self.root = Node()
        self.bit_len = val

    def insert(self, num):
        cur = self.root
     
        for  i in range(self.bit_len, -1, -1):
            bit = 1 if num & (1 << i)else 0
            if cur.children[bit] is None:
                cur.children[bit] = Node()
            cur = cur.children[bit]
            
    def findMax(self, num):
        cur = self.root
        max_num = 0
        for  i in range(self.bit_len, -1, -1):
            bit = 1 if num & (1 << i) else 0
            if cur.children[1 - bit] is not None:
                max_num = max_num | (1 << i)
                cur = cur.children[1 - bit]
            else:
                cur = cur.children[bit]
        return max_num

n = int(sys.stdin.readline().strip())

nums = list(map(int, sys.stdin.readline().strip().split()))

trie = Trie(len(bin(max(nums))))

tot_pref = 0
nums = [0] + nums

for num in nums:
    tot_pref ^= num

cur_pref = 0
ans = 0

for  num in nums:
    cur_pref ^= num
    trie.insert(cur_pref)
    ans = max(ans, trie.findMax(cur_pref ^ tot_pref))

print(ans)