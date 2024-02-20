class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        # (pow(5, n//2))*(pow(4, n//2)) % MOD if not n % 2 else (pow(5, ceil(n/2)))*(pow(4, n//2)) % MOD
        # (a^b) % c = (a^(b % (c-1))) % c , therefore
        return pow(5, (n+1)//2%(MOD-1), MOD)*pow(4, n//2%(MOD-1), MOD) % MOD