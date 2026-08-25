class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min = sorted(strs, key = len)[0]
        ans = ""
        diff = False

        for i in range(len(min)):
            for j in range(len(strs)):
            
                if strs[0][i] != strs[j][i]:
                    diff = True
                    break
            else:
                ans += strs[0][i]
                
            if diff:
                break
            
        return ans