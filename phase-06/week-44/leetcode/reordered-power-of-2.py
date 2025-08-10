class Solution:
    def isPowerofTwo(self, x):
        return x > 0 and log2(x) == int(log2(x))


    def dfs(self, digits, used, num):

        if len(num) == len(digits):
            return self.isPowerofTwo(int(num))

        
        for i in range(len(digits)):
            if (num == "" and digits[i] == "0") or (used & (1 << i)):
                continue

            new_num = num + digits[i]
            new_used = used | (1 << i)

            if self.dfs(digits, new_used, new_num):
                return True

        return False  
            
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = list(i for i in str(n))

        return self.dfs(digits, 0, "")


        
        
