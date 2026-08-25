class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for i in range(n - 1):
            last = s
            new = ""
            for i in last[::-1]:
                if i == "0":
                    new += "1"
                else:
                    new += "0"
            s = last + "1" + new

        return s[k-1]
            
        
