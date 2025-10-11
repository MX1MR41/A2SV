class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # dp
        # group each power along with its frequency and compress the power array like
        # [(power1, freq1), (power2, freq2),...], and sort this array based on power
        # keep track of the maximum damage possible for every index in a dp array
        # for every power, look back to the last three indices which could contain
        # a power which < current_power - 2, in which case we can add the total damage
        # from that index to the damage of our current index,
        # and update the dp array such that dp[i] will have the maximum damage from 0...i
        # it suffices to look at the last three indices because we have sorted the powers
        # if power[i] - 1 and power[i - 2] occur, they will definitely be in the last three
        # indices, in which case we can take the damage from power[i - 3]

        count = Counter(power)
        power = list(sorted(count.items()))

        n = len(power)

        dp = [0] * n

        dp[0] = power[0][0] * power[0][1]

        for i in range(1, n):
            curr_power, curr_count = power[i]
            curr_damage = curr_power * curr_count

            prev_best = 0

            
            if i - 1 >= 0 and power[i - 1][0] < curr_power - 2:
                prev_best = max(prev_best, dp[i - 1])

            if i - 2 >= 0 and power[i - 2][0] < curr_power - 2:
                prev_best = max(prev_best, dp[i - 2])

            if i - 3 >= 0 and power[i - 3][0] < curr_power - 2:
                prev_best = max(prev_best, dp[i - 3])

            dp[i] = curr_damage + prev_best
            dp[i] = max(dp[i], dp[i - 1])

        return max(dp)
