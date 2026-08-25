class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [i for i in nums if i >= 0]
        neg = [i for i in nums if i < 0]
        res = []

        for i in range(len(nums)//2):
            res.append(pos.pop(0))
            res.append(neg.pop(0))

        return res
        