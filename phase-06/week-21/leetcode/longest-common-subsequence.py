class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp
        """
        let X = {X1, X2, X3, ..., Xm}, Y = {Y1, Y2, Y3, ..., Yn}
        let Z = {Z1, Z2, Z3, ..., Zp} be the LCS of X and Y
        if we add a letter V to both X and Y at their ends, V would be part of Z and len(Z) += 1
        so new X = {X1, ..., Xm, Xm + 1}, Y = {Y1, ..., Yn, Yn + 1}, Z = {Z1, ..., Zp, Zp + 1}
        len(Zp + 1) = (len(Zp)) + 1 => (LCS(Xm, Yn)) + 1.

        But if we add V to only either X or Y, V would not become part of Z, so the length of Z
        will not change, But we would choose the maximum length from 
        LCS(Xm + 1, Yn) and LCS(Xm, Yn + 1), because Zp was formed from (Xm, Yn), and Zp + 1 is formed
        from either (Xm + 1, Yn) or (Xm, Yn + 1), i.e. adding V to only either X or Y

        """
        
        m, n = len(text1), len(text2)
        dp = [[0]*n for _ in range(m)]


        for i in range(m):
            a = text1[i]

            for j in range(n):
                b = text2[j]

                if a == b:
                    diag = dp[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0

                    dp[i][j] = 1 + diag

                else:
                    up = dp[i - 1][j] if i - 1 >= 0 else 0
                    left = dp[i][j - 1] if j - 1 >= 0 else 0
                    
                    dp[i][j] = max(up, left)


        return dp[-1][-1]
        
