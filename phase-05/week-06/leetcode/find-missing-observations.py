class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # find the sum of the remaining rolls, 
        # find the average of that sum and populate an answer array with that average,
        # see if there remains any leftover,
        # if so iterate over array and distribute the leftover when possible
        m = len(rolls)
        totm = sum(rolls)
        totn = mean*(n+m) - totm
        if totn < n or (totn + totm) % (n+m):
            return []

        mid = totn//n
        if mid > 6:
            return []


        ans = [mid]*(n)
        ind = 0
        left = totn - mid*n
        while ind < n and left:
            add = 6 - ans[ind]
            if not add:
                ind += 1
            else:
                ans[ind] += min(add, left)
                left -= min(add, left)

        if left:
            return []

        return ans
        
