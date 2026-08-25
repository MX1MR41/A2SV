class Solution:
    def __init__(self):
        self.dp = defaultdict(int)

    def minSteps(self, n: int) -> int:
        # recursion + dp
        # if n is prime, it takes n operations to make n
        # if not, it takes the sum of operstions is tskes to make its divisors

        if n in self.dp: return self.dp[n]
        # base cases
        if n == 1: return 0
        if n == 2: return 2
        # return the smallest divisor of n, if 0 then it is prime
        def prime(x):
            div = 0
            for i in range(2, int(sqrt(x) + 1)):
                if not x % i: 
                    div = i
                    return div

            return div

        div = prime(n)

        if not div: return n

        
        return self.minSteps(n//div) + self.minSteps(div)
        
