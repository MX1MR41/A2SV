class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        pre = defaultdict(int)
        cnt = Counter(nums)

        n = len(nums)

        for i in range(n) :
            x = nums[i]
            pre[x] += i

        res = [0 for _ in range(n)]

        for i in range(n):
            x = nums[i]
            res[i] = pre[x] - (cnt[x] * i)
            pre[x] -= 2 * i
            cnt[x] -= 2

        return res
        