class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = Counter(nums)
        res = [i for i in cnt if cnt[i] > math.floor(n/3)]
        return res
        