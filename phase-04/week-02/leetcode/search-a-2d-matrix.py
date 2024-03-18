class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(arr, x):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r)//2
                curr = arr[mid]
                if curr == x: return True
                elif curr < x: l = mid + 1
                else: r = mid - 1
            return False


        lo, hi = 0, len(matrix) - 1

        while lo <= hi:
            mid = (lo + hi)//2
            curr = matrix[mid]
            if curr:
                if curr[0] <= target <= curr[-1]:
                    return search(curr, target)
                elif target < curr[0]:
                    hi = mid - 1
                else:
                    lo = mid + 1

        return False

        