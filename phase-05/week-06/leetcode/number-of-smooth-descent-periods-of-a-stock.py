class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # a dynamic sliding window approach where we expand if the condition holds
        # else we count the number of subarray in the window we have had so far

        f = lambda x: x*(x+1)//2 # returns number of subarrays in an array of size x

        n = len(prices)

        ans = 0

        l = 0
        for r in range(n):
            # skip single days and we will add them later at the end
            if r == l:
                continue

            # anomaly found: window can't be expanded anymore
            # count subarrays and deduct the length to exclude single elements, to be added later
            if prices[r] != prices[r-1] - 1:
                ans += f(r - l) - (r - l) 
                l = r
                continue

            # handles edge case of counting subarrays at the end of the array
            if r == n-1 and r != l:
                ans += f(r + 1 - l) - (r + 1 - l)



        return ans + len(prices) # add the single elements to the answer
                

        
