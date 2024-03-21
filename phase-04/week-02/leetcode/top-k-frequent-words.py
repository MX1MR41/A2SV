class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        MAX = MIN = 0

        for i in cnt:
            MAX = max(cnt[i], MAX)
            MIN = min(cnt[i], MIN)
        
        RANGE = MAX - MIN

        buckets = [[] for _ in range(RANGE+1)]

        for i in words:
            buckets[cnt[i]].append(i)

        for i in range(len(buckets)):
            SET = sorted(list(set(buckets[i])))
            buckets[i] = SET


        ans = []
        for bucket in buckets[::-1]:
            ans.extend([i for i in bucket])



        return ans[:k]
        