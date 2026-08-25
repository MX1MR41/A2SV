class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        suf_zero = []


        for row in grid:
            z = 0
            for i in range(n - 1, -1, -1):
                if row[i] != 0:
                    break

                z += 1

            suf_zero.append(z)



        swaps = 0

        for i in range(n):
            should_be = n - i - 1
            if suf_zero[i] >= should_be:
                continue

            found = float("inf")
            for j in range(i + 1, n):
                if suf_zero[j] >= should_be:
                    found = j
                    break

            if found == float("inf"):

                return -1

            swaps += found - i

            for j in range(found, i, -1):
                suf_zero[j], suf_zero[j - 1] = suf_zero[j - 1], suf_zero[j]

           
        return swaps
        
        return 1
