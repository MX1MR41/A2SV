class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # prefix sum + dp
        nums = arr
        n = len(arr)
        min_len = [float("inf") for _ in range(n)]
        last_ind = defaultdict(int)
        last_ind[0] = -1

        res = float("inf")

        pre = 0
        for i in range(n):
            num = nums[i]
            pre += num
            deduct = pre - target
            if deduct in last_ind:
                ind = last_ind[deduct]
                length = i - ind
                prev_length = min_len[ind]
                res = min(res, length + prev_length)
                min_len[i] = length
            last_ind[pre] = i
            if i > 0:
                min_len[i] = min(min_len[i], min_len[i - 1])

        return res if res != float("inf") else -1

        
