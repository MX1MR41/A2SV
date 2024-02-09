class Solution:
    def minimumSteps(self, s: str) -> int:
        n =  len(s)
        l, r = 0, n - 1 # left and right pointers to point to leftmost 1s and rightmost 0s respectively
        res = 0

        while l < r:
            if r <= l:
                break

            if s[l] == '1' and s[r] == '0': 
                res += r - l # since the number of swaps is equal to the distance between l and r
                l += 1
                r -= 1

            while l < n and s[l] != '1': # find the next leftmost 1
                l += 1

            while r >= 0 and s[r] != '0': # find the next rightmost 0
                r -= 1

        return res


        