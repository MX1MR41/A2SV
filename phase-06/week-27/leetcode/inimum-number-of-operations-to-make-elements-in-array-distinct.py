class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.reverse()
        cnt = Counter(nums)

        ops = 0

        while len(nums) != len(cnt):
            ops += 1
            for _ in range(min(3, len(nums))):
                num = nums.pop()
                cnt[num] -= 1
                if cnt[num] == 0:
                    del cnt[num]

        return ops
        
