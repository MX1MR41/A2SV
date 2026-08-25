class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # greedy
        # instead of choosing which ballons to remove, we can choose which to keep
        # in a subarray of similar colored balloons, we want to keep the one with
        # the biggest neededTime, so that we can remove the ones with the smaller
        # neededTimes and minimize the cost of removal.
        # so while iterating over that subarray, we keep track of the maximum and keep
        
        keep_time = 0
        prev_time = neededTime[0]

        for i in range(1, len(colors)):

            if colors[i] == colors[i - 1]:
                prev_time = max(prev_time, neededTime[i])
            else:
                # add previous similar balloons subarray max to our time
                keep_time += prev_time
                prev_time = neededTime[i]

        keep_time += prev_time

        remove_time = sum(neededTime) - keep_time

        return remove_time
