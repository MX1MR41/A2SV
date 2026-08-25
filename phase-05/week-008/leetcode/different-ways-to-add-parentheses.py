class Solution:
    def convertToArray(self, expression):
        n = len(expression)
        arr = []
        i, j = 0, -1
        ops = {"+", "-", "*"}
        
        while i < n:
            if expression[i] in ops:
                arr.append(int(expression[j + 1:i]))
                arr.append(expression[i])
                j = i
            i += 1
        arr.append(int(expression[j + 1:]))
        return arr

    def diffWaysToCompute(self, expression: str) -> List[int]:
        # recusion + dp
        # convert expression into array for ease
        # iterate over the array. When operator is found, make a split 
        # and dfs over the left and right part, then compute all possible combinations
        # from both array with the current operator
        # base case is a single number; return that number in a list.
        

        arr = self.convertToArray(expression)
        n = len(arr)
        ops = {"+", "-", "*"}
        dp = defaultdict(int)
        def dfs(l, r):
            if (l, r) in dp: return dp[(l, r)]

            if r == l: return [arr[l]]

            ans = []
            for i in range(l, r):
                if arr[i] in ops:
                    left = dfs(l, i - 1)
                    right = dfs(i + 1, r)
                    for a in left:
                        for b in right:
                            if arr[i] == "+": ans.append(a + b)
                            elif arr[i] == "-": ans.append(a - b)
                            else: ans.append(a * b)
            return ans
        
        return dfs(0, n - 1)
