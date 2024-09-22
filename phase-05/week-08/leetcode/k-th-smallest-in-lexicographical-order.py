class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # instead of building the trie, simulate the traversal process.
        # minimize the search space by narrowing down into the subtree that could have kth
        # by counting the number of steps between a root and the next root.
        
        # function to count the number of steps betweem prefix and prefix + 1
        def countSteps(prefix):
            current = prefix
            next_prefix = prefix + 1
            steps = 0
            while current <= n:
                steps += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return steps
        
        current = 1
        i = 1 

        while i < k:
            steps = countSteps(current)
            if i + steps <= k:
                # skip the current subtree because the answer can't be in it
                current += 1
                i += steps
            else:
                # go deeper into the current subtree
                current *= 10
                i += 1

        return current
