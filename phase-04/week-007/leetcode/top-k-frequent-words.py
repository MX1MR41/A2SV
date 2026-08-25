class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        cnt = Counter(words)
        arr = [(-cnt[i], i) for i in cnt]

        heapify(arr)

        ans = [heappop(arr)[1] for _ in range(k)]

        return ans

