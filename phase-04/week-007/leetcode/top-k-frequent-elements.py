class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        # store the numbers with their frequencies as tuples
        # so that heapify will heapify them based on their frequencies
        arr = [(cnt[i], i) for i in cnt]

        heapify(arr)

        return [i[1] for i in nlargest(k, arr)]
