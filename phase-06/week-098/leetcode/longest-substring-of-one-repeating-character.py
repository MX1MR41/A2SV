class Node:
    # Python feature: removes dictionary overhead, making object attribute access much faster
    __slots__ = ['max', 'data'] 
    
    def __init__(self):
        self.max = 1
        self.data = []

class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n)) if n > 1 else 1
        self.tree = [Node() for _ in range(2 * self.n)]

    def update(self, ind, val):
        ind += self.n

        self.tree[ind].data = [(val, 1)]
        self.tree[ind].max = 1

        par = ind // 2

        while par > 0:
            left = self.tree[2 * par]
            right = self.tree[2 * par + 1]
            
            maxx = left.max if left.max > right.max else right.max

            ld = left.data
            rd = right.data

            # Early building check: if a node is completely empty
            if not ld:
                self.tree[par].data = rd
                self.tree[par].max = maxx
            elif not rd:
                self.tree[par].data = ld
                self.tree[par].max = maxx

            # Merge if left's suffix matches right's prefix
            elif ld[-1][0] == rd[0][0]:
                merged_freq = ld[-1][1] + rd[0][1]
                if merged_freq > maxx:
                    maxx = merged_freq
                
                # Because max length is 2, we can just assign the combinations directly
                # avoiding ANY loops or array creation overhead
                if len(ld) == 1 and len(rd) == 1:
                    self.tree[par].data = [(ld[0][0], merged_freq)]
                elif len(ld) == 1:
                    self.tree[par].data = [(ld[0][0], merged_freq), rd[-1]]
                elif len(rd) == 1:
                    self.tree[par].data = [ld[0], (rd[0][0], merged_freq)]
                else:
                    self.tree[par].data = [ld[0], rd[-1]]
            else:
                # No merge possible, take left's prefix and right's suffix
                self.tree[par].data = [ld[0], rd[-1]]

            self.tree[par].max = maxx
            par //= 2

    def queryMax(self):
        return self.tree[1].max


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        # modified segment tree
        # we need to perform quick updates and quick queries - ergo segment tree are fit for this
        # when merging two nodes, we check if the place they meet has the same letter,
        # in which case we can add up their frequencies. 
        # And we only need to store the rightmost and leftmost group of similar letter for each node
        # because those are the ones that could changes result by merging as we move up the tree
        n = len(s)
        tree = SegmentTree(n)

        # Build initial tree
        for i in range(n):
            tree.update(i, s[i])

        res = []
        # Process Queries
        for i in range(len(queryIndices)):
            tree.update(queryIndices[i], queryCharacters[i])
            res.append(tree.queryMax())

        return res
