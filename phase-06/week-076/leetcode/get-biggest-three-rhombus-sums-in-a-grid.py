class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set() # A set naturally handles duplicates
        
        for i in range(m):
            for j in range(n):
                # Area 0 rhombus (just the single cell)
                sums.add(grid[i][j])
                
                # Check larger rhombuses with their Top corner at (i, j)
                L = 1
                # Ensure the bottom, left, and right corners are in bounds
                while i + 2 * L < m and j - L >= 0 and j + L < n:
                    curr_sum = 0
                    
                    # 1. Walk from Top to Right
                    for k in range(L):
                        curr_sum += grid[i + k][j + k]
                        
                    # 2. Walk from Right to Bottom
                    for k in range(L):
                        curr_sum += grid[i + L + k][j + L - k]
                        
                    # 3. Walk from Bottom to Left
                    for k in range(L):
                        curr_sum += grid[i + 2 * L - k][j - k]
                        
                    # 4. Walk from Left to Top
                    for k in range(L):
                        curr_sum += grid[i + L - k][j - L + k]
                        
                    sums.add(curr_sum)
                    L += 1 # Expand the rhombus size
                    
        # Sort distinct sums in descending order and grab the top 3
        return sorted(list(sums), reverse=True)[:3]
