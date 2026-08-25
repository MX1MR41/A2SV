class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = defaultdict(int)
        count = 0
        n = len(arr)
        for i, num in enumerate(arr):
            key = k - (num % k)
            if cnt[key]:
                count += 1
                cnt[key] -= 1
            else:
                cnt[(num % k) or k] += 1
        return count == n // 2