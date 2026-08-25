class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        nonce = once = twice = thrice = True

        n = len(mat)

        for i in range(n):
            for j in range(n):

                cell = mat[i][j]

                rot0 = target[i][j]
                if cell != rot0:
                    nonce = False

                rot1 = target[j][n - i - 1]
                if cell != rot1:
                    once = False

                rot2 = target[n - i - 1][n - j - 1]
                if cell != rot2:
                    twice = False

                rot3 = target[n - j - 1][i]
                if cell != rot3:
                    thrice = False



        return nonce or once or twice or thrice
        
