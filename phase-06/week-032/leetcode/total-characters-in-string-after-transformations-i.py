class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # dp 
        # count transformation by transformation
        MOD = 10**9 + 7


        prev_count = [0] * 26
        for i in s:
            prev_count[ord(i) - 97] += 1

        for _ in range(t):
            new_count = [0] * 26

            for i in range(26):
                letter = chr(i + 97)

                if letter == "z":
                    new_count[0] = (new_count[0] + prev_count[-1]) % MOD
                    new_count[1] = (new_count[1] + prev_count[-1]) % MOD

                else:
                    new_count[i + 1] = (
                        new_count[i + 1] + prev_count[i]
                    ) % MOD

            prev_count = new_count

        res = 0

        for freq in prev_count:
            res = (res + freq) % MOD

        return res
