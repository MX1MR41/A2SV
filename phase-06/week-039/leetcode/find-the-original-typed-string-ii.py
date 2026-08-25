class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(word)

        run_lengths = []
        run_len = 1
        for i in range(1, n):
            if word[i] == word[i - 1]:
                run_len += 1
            else:
                run_lengths.append(run_len)
                run_len = 1
        run_lengths.append(run_len)

        total_ways = 1
        for length in run_lengths:
            total_ways = total_ways * length % MOD

        if len(run_lengths) >= k:
            return total_ways

        dp = [1] + [0] * (k - 1)

        prefix = [1] * k

        for length in run_lengths:
            new_dp = [0] * k

            for j in range(1, k):
                new_dp[j] = prefix[j - 1]
                if j - length - 1 >= 0:
                    new_dp[j] = (new_dp[j] - prefix[j - length - 1]) % MOD

            new_prefix = [new_dp[0]]
            for j in range(1, k):
                new_prefix.append((new_prefix[-1] + new_dp[j]) % MOD)

            dp, prefix = new_dp, new_prefix

        return (total_ways - prefix[k - 1]) % MOD
