"""

https://codeforces.com/gym/526229/problem/C

"""

class TrieNode:
    def __init__(self):
        self.ch = [None, None]
        self.is_end = False 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, length):
        stack, trie = [], self.root 
        word = []
        
        for i in range(length):
            stack.append(trie) 
            if trie.ch[0] is None or not trie.ch[0].is_end:
                if trie.ch[0] is None:
                    trie.ch[0] = TrieNode()
                trie = trie.ch[0]
                word.append('0')
            elif trie.ch[1] is None or not trie.ch[1].is_end:
                if trie.ch[1] is None:
                    trie.ch[1] = TrieNode()
                trie = trie.ch[1]
                word.append('1')
            else:
                return False
        trie.is_end = True

        
        while stack and stack[-1].ch[1] and stack[-1].ch[1].is_end:
            prev = stack.pop()
            prev.is_end = True

        return ''.join(word)


n = int(input())    
nums = sorted(zip(map(int, input().split()), range(n)))
trie = Trie()
words = [''] * n
for num, indx in nums:
    word = trie.insert(num)
    if not word:
        print('NO')
        exit()
    words[indx] = word

print('YES')
for word in words:
    print(word)
