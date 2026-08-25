class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
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

                print(arr)

        cnt = Counter(nums)
        length = len(nums)
        for i in range(length):
            if nums[i] == val:
                nums[i] = "_"


        move(nums)

        return length - cnt[val]
        