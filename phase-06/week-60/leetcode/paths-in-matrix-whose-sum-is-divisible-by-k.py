class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        # dynamic programming dp
        # 3D dp
        # since k is only as big as 50, for each cell we can store an array of size k
        # where array[i] is the number of ways you can reach to the last cell 
        # where the path sum % k == i.

        m, n = len(grid), len(grid[0])

        mod_grid = [[[0 for _ in range(k)] for _ in range(n)] for _ in range(m)]


        # traverse backwards and upwards
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                curr_mod = grid[i][j] % k
                curr_k = mod_grid[i][j]
                
                # base case: the last cell
                if (i, j) == (m - 1, n - 1):
                    curr_k[curr_mod] = 1
                    continue

                # has a cell below it
                if i + 1 < m:
                    next_k = mod_grid[i + 1][j]
                    for mod in range(k):
                        if next_k[mod] > 0:

                            # if we sum two numbers x and y where x % k = a and y % k = b
                            # then (x + y) % k => ((x % k) + (y % k)) % k 
                            # so basically just sum up the mods of the addends 
                            new_mod = (curr_mod + mod) % k

                            # if there were x ways for next_k[mod], then curr_k[new_mod]
                            # can use those ways so we add them
                            curr_k[new_mod] += next_k[mod]

                # has a cell to its right
                if j + 1 < n:
                    next_k = mod_grid[i][j + 1]
                    for mod in range(k):
                        if next_k[mod] > 0:
                            new_mod = (curr_mod + mod) % k
                            curr_k[new_mod] += next_k[mod]



        return mod_grid[0][0][0] % 1000000007
        
