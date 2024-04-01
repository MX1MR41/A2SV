class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        left, right = [], []
        end = int(n**0.5) + 1
        for i in range(1,end):
            if not n % i:
                j = n//i
                if i != j:
                    left.append(i)
                    right.append(j)
                else:
                    left.append(i)

        factors = left + right[::-1]
        n = len(factors)
        return factors[k-1] if k <= n else -1

        
