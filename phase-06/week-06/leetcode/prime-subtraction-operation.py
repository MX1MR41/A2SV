class Solution:
    def __init__(self):
        # sieve of eratosthenes to sieve out prime numbers upt 1000
        limit = 1000
        is_prime = [True] * (limit + 1)
        is_prime[0], is_prime[1] = False, False 

        # iterating upto the square root will suffice
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                # start from i*i since i*(i-1), i*(i-2)... will have already been computed
                # jump by i, essentially adding i every time
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False

        self.primes = [i for i, prime in enumerate(is_prime) if prime]



    def primeSubOperation(self, nums: List[int]) -> bool:
        # binary search

        n = len(nums)

        for i in range(n-2, -1, -1):

            curr, nxt = nums[i], nums[i+1]

            if curr >= nxt:
                # first find the upper limit for the binary search using binary search
                # i.e. the greatest prime number less than curr and assign it to "right"
                start, end = 0, len(self.primes) - 1
                right = 0
                while start <= end:
                    mid = (start + end)//2
                    if self.primes[mid] < curr:
                        right = mid
                        start = mid + 1
                    else:
                        end = mid - 1


                # now do binary search to find the smallest prime needed to be deducted from curr
                # so curr can become less than nxt
                left = ans = 0
                while left <= right:
                    mid = (left + right)//2
                    
                    new = curr - self.primes[mid]

                    if new < nxt:
                        ans = mid
                        right = mid - 1
                    else:
                        left = mid + 1

                if self.primes[ans] < curr:
                    nums[i] = curr - self.primes[ans]

        return all([nums[i] < nums[i+1] for i in range(n - 1)])


        
        
