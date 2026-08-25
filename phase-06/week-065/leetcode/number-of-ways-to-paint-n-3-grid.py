class Solution:
    def numOfWays(self, n: int) -> int:
        # dynamic programming
        # there are generally two coloring patterns for a row:- ABC and ABA
        # and each ABC generates new 2 ABC's and 2 ABA's, total of 4 for the next row
        # and each ABA generates new 2 ABC's and 3 ABA's, total of 5 for the next row
        # to compute the total for current row, we just count the total contributions
        # of the previous ABC and ABA patterns by doing 4*ABC + 5*ABA respectively
        # then to prepare for the next row, we count the new patterns that each current
        # pattern we have can generate

        total = 12
        ABC = ABA = 6

        MOD = 1000000007

        for i in range(2, n + 1):
            total = (4*ABC + 5*ABA) % MOD
            
            next_ABC = (2*ABC + 2*ABA) % MOD
            next_ABA = (2*ABC + 3*ABA) % MOD

            ABC = next_ABC
            ABA = next_ABA

        return total
        
