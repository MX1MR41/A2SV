"""

https://codeforces.com/gym/544854/problem/D

"""

import sys
input = lambda: sys.stdin.readline().rstrip()

class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.position = -1 # index of the corresponding number in the given array

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans_i = ans_j = ans_x = 1, 1, 0
    max_val = 0 # maximum value of (a[i] ^ x) & (a[j] ^ x)
    
    root_node = TrieNode()
    for i, num in enumerate(a):
        cur_node = root_node
        # find a pair a[j] for this number
        # first check if there's at least one number in the trie
        if cur_node.children[0] or cur_node.children[1]:
            x = 0
            for bit_i in range(k - 1, -1, -1):
                if num & (1 << bit_i):
                    # match 1 bit with 1 bit
                    if cur_node.children[1]:
                        cur_node = cur_node.children[1]
                    else: # if not possible, match 1 bit with 0 bit
                        cur_node = cur_node.children[0]

                else:
                    # match 0 bit with 0 bit
                    if cur_node.children[0]:
                        cur_node = cur_node.children[0]
                        x = x ^ (1 << bit_i)
                    else: # if not possible, match 0 bit with 1 bit
                        cur_node = cur_node.children[1]

            j = cur_node.position
            new_val = (num ^ x)&(a[j] ^ x)
            if new_val >= max_val:
                max_val = new_val
                ans_i, ans_j, ans_x = i + 1, j + 1, x

        # insert the current number into the trie
        cur_node = root_node
        for bit_i in range(k - 1, -1, -1):
            if num & (1 << bit_i):
                if not cur_node.children[1]:
                    cur_node.children[1] = TrieNode()
                cur_node = cur_node.children[1]

            else:
                if not cur_node.children[0]:
                    cur_node.children[0] = TrieNode()
                cur_node = cur_node.children[0]

        cur_node.position = i

    print(ans_i, ans_j, ans_x)

    