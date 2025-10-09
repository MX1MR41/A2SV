class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        # simulation + dp
        # keep track of the earliest time that each wizard will be available for work
        # simulate the process by brewing potion by potion
        # traverse from the last wizard backwards, maximizing the the availabilty of each wizard
        # based on how early his successor will be free, leaving no time gaps
        # now traverse from the first wizard forwards, brewing potions and updating availability

        n = len(skill)
        available = [0] * n

        for potion in mana:
            # preprocessing
            brewing_time = [wiz * potion for wiz in skill]

            for i in range(n - 2, -1, -1):
                # the earliest that this wizard can start brewing is the earliest the next wizard
                # will be available minus the brewing time of this potion
                # that way, when this wizard is done, the next will start immediately
                start_time = available[i + 1] - brewing_time[i]
                if start_time > available[i]:
                    available[i] = start_time


            # brew
            available[0] += brewing_time[0]
            prev = available[0]
            for i in range(1, n):
                # this wizard's start time is earlier than the previous wizard's finish time
                if prev > available[i]:
                    available[i] = prev

                available[i] += brewing_time[i]
                prev = available[i]

        return available[-1]
