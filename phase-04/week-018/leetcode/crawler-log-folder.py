class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []
        for i in logs:
            if i == "../": 
                if stk:
                    stk.pop()
            elif i == "./":
                continue
            else:
                stk.append(i)

        return len(stk)
        
