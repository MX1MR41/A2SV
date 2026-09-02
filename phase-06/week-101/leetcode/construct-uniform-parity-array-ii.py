class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        mino = float("inf")
        for i in nums1:
            if i % 2:
                mino = min(i, mino)

        even = 0
        for i in nums1:
            if not i % 2:
                even += 1
            else:
                if mino < i:
                    even += 1



        odd = 0
        for i in nums1:
            if i % 2:
                odd += 1
            else:
                if mino < i:
                    odd += 1



        return even == n or odd == n


