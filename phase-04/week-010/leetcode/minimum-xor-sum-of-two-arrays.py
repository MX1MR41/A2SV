class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        # backtracking + dp + bitmanipulation
        # create an nxn grid of where grid[i][j] = nums[i] ^ nums[j]
        # we use a mask to keep track of indices that have already been used
        n = len(nums1)
        grid = [[0]*n for _ in range(n)]

        for i in range(n):
            a = nums1[i]
            for j in range(n):
                b = nums2[j]
                grid[i][j] = a ^ b

        dp = defaultdict(int)

        def dfs(i, j, mask):
            if i == n: return 0 # array exhausted

            mask |= 1 << j # set bit j as 1 to inidcate that index j has been visited

            if (j, mask) in dp: return dp[(j,mask)]

            curr = grid[i][j]
            temp = float("inf")
            for col in range(n):
                if not (mask & (1 << col)):
                    temp = min(temp, dfs(i + 1, col, mask))

            dp[(j,mask)] = curr + temp if temp != float("inf") else curr

            return dp[(j,mask)]

        ans = float("inf")

        for i in range(n):
            ans = min(ans, dfs(0, i, 0))

        return ans
