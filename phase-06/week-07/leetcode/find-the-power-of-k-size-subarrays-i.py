class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []

        n = len(nums)
        for i in range(n - k + 1):
            sub = []
            for j in range(i, i + k):
                if sub and sub[-1] != nums[j] - 1:
                    ans.append(-1)
                    break
                else:
                    sub.append(nums[j])

            else:
                ans.append(sub[-1])

        return ans
