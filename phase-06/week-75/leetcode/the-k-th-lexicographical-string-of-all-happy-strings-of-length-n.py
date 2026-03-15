class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        prev = 0
        res = ""
        for i in range(n):
            # 1. The block size halves at each step
            block_size = 2 ** (n - 1 - i)
            
            if i == 0:
                # First character: 3 choices
                a = prev + 1 * block_size
                b = prev + 2 * block_size
                c = prev + 3 * block_size
                
                if k <= a:
                    res += "a"
                    # 3. Don't set prev = 0, leave it unchanged
                elif k <= b:
                    res += "b"
                    prev = a
                elif k <= c:
                    res += "c"
                    prev = b
                else:
                    return ""
            else:
                # 2. Subsequent characters: only 2 valid choices
                choices = [ch for ch in ['a', 'b', 'c'] if ch != res[-1]]
                
                a = prev + 1 * block_size
                b = prev + 2 * block_size
                
                if k <= a:
                    res += choices[0]
                    # Leave prev unchanged
                elif k <= b:
                    res += choices[1]
                    prev = a
                else:
                    return ""

        # 4. Safe to return res, out-of-bounds handled in i == 0
        return res
