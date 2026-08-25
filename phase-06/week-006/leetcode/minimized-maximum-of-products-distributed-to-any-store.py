class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # binary search + stack
        # validate a choice by checking if it is possible to distriute ALL products to each store
        # with a maximum value of choice
        total = sum(quantities)
        def distribute(x):
            distributed_to = 0
            for prod in quantities:
                distributed_to += ceil(prod/x)

            if distributed_to > n:
                return False
            else:
                return True

            
        l, r = 1, 10**5
        ans = r
        while l <= r:
            mid = (l + r)//2
            if distribute(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans


        
