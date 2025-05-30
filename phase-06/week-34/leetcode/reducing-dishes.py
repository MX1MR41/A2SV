class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # greedy + sorting

        satisfaction.sort(reverse = True)

        def like_time_sum(k):
            dishes = satisfaction[:k]
            tot = sum([(k - i) * dishes[i] for i in range(k)])

            return tot

        res = 0
        for i in range(len(satisfaction) + 1):
            res = max(res, like_time_sum(i))

        return res
