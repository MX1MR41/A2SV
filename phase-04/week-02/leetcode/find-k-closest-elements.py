class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ind = bisect_left(arr, x)
        n = len(arr)
        if ind == 0:
            return arr[:k]
        elif ind == n:
            return arr[n-k:]
        else:
            l, r = ind - 1, ind
            while r - l - 1 < k:
                if l < 0:
                    r += 1
                elif r >= n:
                    l -= 1
                elif abs(arr[l] - x) <= abs(arr[r] - x):
                    l -= 1
                else:
                    r += 1

            return arr[l+1:r]
