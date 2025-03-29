class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # monotonic stack + heap + prime numbers
        n = len(nums)
        MOD = 10**9 + 7
        
        # efficient prime factors counting
        prime_scores = [0] * n
        for i, num in enumerate(nums):
            cnt = 0
            temp = num
            d = 2
            # while we still haven't reached the square root of temp
            while d * d <= temp:
                if temp % d == 0: # found a prime factor
                    cnt += 1
                    # keep factorizing it by this prime factor, so the next number that will divide
                    # temp will be a prime number
                    while temp % d == 0:
                        temp //= d
                d += 1

            if temp >= 2:
                cnt += 1

            prime_scores[i] = cnt

        next_dominant = [n] * n
        prev_dominant = [-1] * n

        # monotonic stack for efficient range calculation
        stack = []
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                top = stack.pop()
                next_dominant[top] = i
            if stack:
                prev_dominant[i] = stack[-1]
            stack.append(i)

        num_of_subarrays = [(next_dominant[i] - i) * (i - prev_dominant[i]) for i in range(n)]
        
        # use heap to greedily choose the biggets numbers
        heap = []
        for i in range(n):
            heapq.heappush(heap, (-nums[i], i))
        
        score = 1
        while k > 0:
            num, i = heapq.heappop(heap)
            num = -num
            use = min(k, num_of_subarrays[i])
            score = (score * pow(num, use, MOD)) % MOD
            k -= use
        return score
