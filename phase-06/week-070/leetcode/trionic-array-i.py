class Solution:
    def isTrionic(self, nums: List[int]) -> bool:

        def check(d, l, r):
            if d:
                for i in range(l + 1, r + 1):
                    if nums[i] <= nums[i - 1]:
                        return False

                return True

            else:
                for i in range(l + 1, r + 1):
                    if nums[i] >= nums[i - 1]:
                        return False

                return True

        n = len(nums)
        for i in range(1, n):
            for j in range(i + 1, n - 1):
                if check(True, 0, i) and check(False, i, j) and check(True, j, n -1):
                    return True

        return False


