class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ANSWER = [0 for _ in range(len(nums))]

        def merge_sort(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])

            return merge(left, right)

        def merge(left, right):
            res = []
            l, r = 0, 0

            while l < len(left) or r < len(right):
                if r >= len(right) or (l < len(left) and left[l][1] <= right[r][1]):
                    res.append(left[l])
                    ANSWER[left[l][0]] += r
                    l += 1
                else:
                    res.append(right[r])
                    r += 1

            return res

        merge_sort(list(enumerate(nums)))
        
        return ANSWER
