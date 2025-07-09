class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # greedy + sliding window
        # [gap 1][meet 1][gap 2][meet 2][gap 3][meet 3]...
        # if you move [meet 1] and [meet 2] to the far left, the format would be
        # [meet 1][meet 2][gap 1][gap 2][gap 3][meet 3]
        # so moving k meeting around is a matter of combining k + 1 gaps to create 
        # a bigger gap and hence more free time. So the problem boils down to 
        # maximum subarray sum of size k where the elements are [gap 1][gap 2][gap 3]..
        
        n = len(startTime)

        free_times = []
        free_times.append(startTime[0])

        for i in range(1, n):
            free_times.append(startTime[i] - endTime[i - 1])

        free_times.append(eventTime - endTime[-1])


        res = 0
        curr = 0
        l = 0
        for r in range(len(free_times)):
            curr += free_times[r]

            while r - l + 1 > k + 1:
                curr -= free_times[l]
                l += 1

            res = max(res, curr)

        return res

