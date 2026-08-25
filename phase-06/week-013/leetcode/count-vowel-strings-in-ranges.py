# PREFIX SUM SOLUTION

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # prefix sum
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        def vowelString(word):
            return word[0] in vowels and word[-1] in vowels

        prefix_sum = []
        pre = 0
        for word in words:
            if vowelString(word):
                pre += 1

            prefix_sum.append(pre)

        res = []
        for l, r in queries:
            if l == 0:
                res.append(prefix_sum[r])
            else:
                res.append(prefix_sum[r] - prefix_sum[l - 1])

        return res




# SEGMENT TREE SOLUTION

class SegmentTree:
    def __init__(self, arr):
        self.n = 2 ** (ceil(log2(len(arr))))
        self.tree = [0] * (2 * self.n)

        for i in range(len(arr)):
            self.tree[self.n + i] = arr[i]

        self.build(1)

    def build(self, index):
        if index >= self.n:
            return self.tree[index]

        self.tree[index] = self.build(2 * index) + self.build(2 * index + 1)
        return self.tree[index]

    def update(self, index, val):
        index += self.n
        self.tree[index] = val

        if index % 2:
            index = (index - 1) // 2
        else:
            index //= 2

        while index > 0:
            self.tree[index] = self.tree[2 * index] + self.tree[s * index + 1]
            if index % 2:
                index = (index - 1) // 2
            else:
                index //= 2

    def query(self, left, right):
        left += self.n
        right += self.n

        extra = 0
        while left < right:
            if left % 2:
                extra += self.tree[left]
                left = (left + 1) // 2
            else:
                left //= 2
            
            if not right % 2:
                extra += self.tree[right]
                right = (right - 2) // 2

            else:
                right = (right - 1) // 2

        return self.tree[left] + extra if left == right else extra

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # segment tree
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        def vowelString(word):
            return word[0] in vowels and word[-1] in vowels

        arr = [1 if vowelString(word) else 0 for word in words ]

        tree = SegmentTree(arr)

        res = []
        for l, r in queries:
            res.append(tree.query(l, r))

        return res
        
