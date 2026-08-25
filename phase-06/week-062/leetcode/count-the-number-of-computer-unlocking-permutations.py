class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        # as long as the first computer has the lowest complexity,
        # then it is possible to just rearrange the remaining computers in any perm

        minn = complexity[0]

        n = len(complexity)


        for i in range(1, n):
            if complexity[i] <= minn:
                return 0

        
        return factorial(n - 1) % 1000000007
