class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        step = len(nums)//2

        for i in range(step):
            result.append(nums[i])
            result.append(nums[i + step])

        return result

        
        