class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 1
        
        curr_len = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                curr_len += 1
            else:
                curr_len = 1
            res = max(res, curr_len)

        # 2. Check for pairs: (a,b), (b,c), (a,c)
        # Helper function: treats 'forbidden' char as a reset wall
        def check_pair(c1, c2, forbidden):
            nonlocal res
            diff = 0
            mp = {0: -1} 
            
            for i, char in enumerate(s):
                if char == forbidden:
                    diff = 0
                    mp = {0: i} 
                elif char == c1:
                    diff += 1
                elif char == c2:
                    diff -= 1
                
                if diff in mp:
                    res = max(res, i - mp[diff])
                else:
                    mp[diff] = i

        check_pair('a', 'b', 'c') 
        check_pair('b', 'c', 'a') 
        check_pair('a', 'c', 'b') 

        mp = {(0, 0): -1}
        a = b = c = 0
        for i, char in enumerate(s):
            if char == 'a': a += 1
            elif char == 'b': b += 1
            else: c += 1
            
            key = (a - b, b - c)
            
            if key in mp:
                res = max(res, i - mp[key])
            else:
                mp[key] = i
                
        return res
