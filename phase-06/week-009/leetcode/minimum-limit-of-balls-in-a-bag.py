class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # binary search
        # key words: "... MINIMIZE ... MAXIMIZE ..."
        
        def check(x):
            ops = 0
            for num in nums:
                ops += ceil(num/x)

            
            return ops <= maxOperations + len(nums)

            


        l, r = 1, max(nums)

        ans = float("inf")

        while l <= r:
            mid = (l + r)//2
            if check(mid):
                ans = mid
                r = mid - 1

            else:
                l = mid + 1

        return ans






        
