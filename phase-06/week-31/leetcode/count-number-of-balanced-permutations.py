class Solution:
    """
    (a / b) % m != (a % m) / (b % m)
    (a / b) % m = (a * inverse(b)) % m =, where inverse(b) is the modular multiplicative inverse of b
    modular inverse of a number b is such a number x where (b * x) % m = 1
    from Fermat's little theorem, (b**(m - 1)) % m = 1, (b * (b ** (m - 2))) % m = 1
    therefore x = (b ** (m - 2)) % m
    so to compute (s!/(f1! * f2!)) % m, we use the inverses of f1 and f2 as follows
    (s! * inverse(f1!) * inverse(f2!)) % m 

    """
    def countBalancedPermutations(self, num: str) -> int:
        # dp + combinatorics
        # count how many ways to pick half of the digits so their sum = half of total,
        # then multiply by permutations of each half and divide out duplicates
        # if the first subset has size s1 and has nums which occur f1, f2, and f3 times,
        # the total unique permutation can be calculated as s1!/(f1! * f2! * f3!), dividing by 
        # factorials of the frequencies of each num to get rid of repetitions
        # the second subset can be calculated as n - s1 = s2, and the remaining frequencies too
        # for subset 2 s2!/(f4! * f5!), then the total ways is going to be
        # ways to permute s1 x ways to permute s2 = (s1!/(f1! * f2! * f3!)) * (s2!/(f4! * f5!))
        # => s1! * s2! / (f1! * f2! * f3! * f4! * f5!)
        # precompute factorials and modular inverses
        
        MOD = 10**9 + 7
        n = len(num)
        
        # total sum of all digits; if odd, no balanced split possible
        total = sum(int(c) for c in num)
        if total % 2:
            return 0
        
        # precompute factorials and inverse factorials for permutation counts
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        
        invfact = [1] * (n + 1)
        for i in range(1, n + 1):
            invfact[i] = pow(fact[i], 10**9 + 5, MOD)
        
        halfSum = total // 2
        halfLen = n // 2
        
        # dp[s][k] = number of ways to choose k digits summing to s
        dp = [[0] * (halfLen + 1) for _ in range(halfSum + 1)]
        dp[0][0] = 1
        
        # count frequency of each digit for later duplicate handling
        digits = [0] * 10
        
        # build subset-sum DP over counts and sums
        for c in num:
            d = int(c)
            digits[d] += 1

            # move backwards to avoid overcounting a single digits contributions
            for summ in range(halfSum, -1, -1):
                for length in range(halfLen, -1, -1):

                    if dp[summ][length] > 0:
                        new_length = length + 1
                        new_sum = summ + d

                        if new_sum <= halfSum and new_length <= halfLen:
                            dp[new_sum][new_length] = (dp[new_sum][new_length] + dp[summ][length]) % MOD

        
        # number of ways to choose halfLen digits summing to halfSum
        res = dp[halfSum][halfLen]
        

        # multiply by permutations of positions in each half
        # res = ways to get dp[halfSum][halfLen] * (s1! * s2!)
        res = (res * (fact[halfLen] * fact[n - halfLen])) % MOD    

        # divide out overcount from identical digits across entire string
        # (f1! * f2! * f3! * f4! * f5!)
        for cnt in digits:
            res = res * invfact[cnt] % MOD
        
        return res
