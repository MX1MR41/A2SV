class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0
        for player in range(1, n+1):
            winner = (winner + k) % player

        return winner + 1

        
