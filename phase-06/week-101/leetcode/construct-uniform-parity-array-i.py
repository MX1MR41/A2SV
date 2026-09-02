class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        o = e = 0
        for i in nums1:
            if i % 2:
                o += 1
            else:
                e += 1


        return (
            (o == n or e >= 1)
            or (e == n or o >= 1)
        )
