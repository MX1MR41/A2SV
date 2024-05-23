class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def dfs(ind, cnt):
            if ind >= n:
                return 1

            temp = dfs(ind + 1, cnt)

            if not cnt[nums[ind] - k] and not cnt[nums[ind] + k]:
                cnt[nums[ind]] += 1
                temp += dfs(ind + 1, cnt)
                cnt[nums[ind]] -= 1

            return temp

        return dfs(0, defaultdict(int)) - 1
        
