class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # modified code from https://leetcode.com/problems/move-zeroes/
        # it will move the "_"s to the end of the list
        def move(arr: List[int]) -> None:
            u , n = 0, 0 
            l = len(arr)
            while u < l and n < l:
                while u < n and arr[u] != "_": 
                    u += 1
                if arr[n] != "_": 
                    arr[u], arr[n] = arr[n], arr[u]
                    u += 1
                n += 1

        k = len(set(nums))
        i = 0
        n = len(nums)
        while i < n:
            num = nums[i]
            j = i + 1 # the next consecutive element
            
            # change all similar numbers to "_"
            while j < n and nums[j] == num:
                nums[j] = "_"
                j += 1

            i = j

        move(nums)

        return k

        