class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        MAX = MIN = 0

        for i in cnt:
            MAX = max(cnt[i], MAX)
            MIN = min(cnt[i], MIN)
        
        RANGE = MAX - MIN

        buckets = [set() for _ in range(RANGE+1)]

        for i in nums:
            buckets[cnt[i]].add(i)



        ans = []
        for bucket in buckets[::-1]:
            ans.extend([i for i in bucket])



        return ans[:k]

        