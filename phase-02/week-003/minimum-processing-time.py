class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        n = len(tasks)
        ans = 0

        # the processor at this iteration ans task
        proc, t =len(processorTime) - 1, 0 

        while t < n:
            m = max(tasks[t: t+4])
            p = processorTime[proc]

            time = p + m
            ans = max(ans, time)

            proc -= 1
            t += 4

        return ans      