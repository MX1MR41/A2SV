class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def count(arr):
            n = len(arr)
            l, r = 0, n - 1 
            res = 0

            while l <= r:
                mid = (l + r)//2
                if arr[mid] < 0:
                    res = n - mid
                    r = mid - 1
                else:
                    l = mid + 1

            return res


        return sum(count(arr) for arr in grid)

        
