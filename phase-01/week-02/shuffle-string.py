class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = [0] * len(s)
        answer = ""
        
        for i in range(len(s)):
            shuffled[indices[i]] = s[i]

        for j in shuffled:
            answer += j

        return answer
