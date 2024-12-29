"""

https://codeforces.com/gym/576323/problem/A

PASSED

"""

from collections import deque


class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = dict()

class Trie:
    def __init__(self):
        self.trie = TrieNode()


    def add(self, num):
        node = self.trie

        for n in num:
            if n not in node.children:
                node.children[n] = TrieNode()
            node = node.children[n]
            node.count += 1

            # print(n, "count =", node.count, node.children)


trie = Trie()

n = int(input())

for _ in range(n):
    num = input()
    trie.add(num)

    # print("_"*20)

que = deque()
length = 0

for ch in trie.trie.children:
    # print(ch, ch.count)
    if trie.trie.children[ch].count == n:
        que.append(trie.trie.children[ch])

# print(que)

while que:
    length += 1
    for _ in range(len(que)):
        node = que.popleft()
        for ch in node.children:
            if node.children[ch].count == n:
                que.append(node.children[ch])

print(length)



