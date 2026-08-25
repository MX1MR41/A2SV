class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr)//2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            ans = merge(left, right)
            return ans

        def merge(left, right):
            l = r = 0

            ans = []
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    ans.append(left[l])
                    l += 1
                else:
                    ans.append(right[r])
                    r += 1

            ans += left[l:]
            ans += right[r:]

            return ans

        return mergeSort(nums)
        
