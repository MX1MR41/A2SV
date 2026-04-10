class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # dp + prefix sum
        MOD = 1000000007
        n = len(nums)

        # PART 1: THE HEAVY/LIGHT DECOMPOSITION STRATEGY
        # We split queries based on the step size 'k'.
        # For large 'k', direct simulation is fast enough.
        # For small 'k', we batch them for an efficient offline approach.
        # The optimal threshold to balance the workload between these two
        # strategies is sqrt(n).
        # heavy queries = Q, max operation of heavy query = n/threshold
        # max operation of all light queries = threshold * n since we would have only threshold of them
        # total complexity will be (Q * (n / threshold) + threshold * n)
        # since Q == n (10^5), (n^2 / threshold + threshold * n)
        # to minimize this sum we need to make the terms equal, this yields threshold = sqrt(n)
        threshold = int(sqrt(n)) + 1 # +1 is a safe habit to avoid edge cases

        # A dictionary to group all "light" queries by their step size 'k'.
        # qs[k] will hold a list of all queries with step k.
        qs = defaultdict(list)

        for l, r, k, v in queries:
            # This is a "heavy" query.
            if k >= threshold:
                # The number of operations is n/k, which is small since k is large.
                # So, we apply it directly to the nums array.
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % MOD
            else:
                # This is a "light" query. We don't apply it yet.
                # We save it to be processed in a batch with others of the same k.
                qs[k].append((l, r, v))

        # PART 2: PROCESSING THE "LIGHT" QUERIES
        # We iterate through each small k that had at least one query.
        for k, k_queries in qs.items():
            
            # prefix sum (difference array)
            p = [1] * n

            # Build a "lane-based" difference array.
            # For each query, we mark the start and end of its range.
            for l, r, v in k_queries:

                start = l

                steps = r - l
                distance = (steps // k) * k

                # The range ends at the last valid index <= r.
                # The "undo" operation must happen at the NEXT index in this lane.
                end = start + distance
                end_plus_one = end + k

                
                p[start] = (p[start] * v) % MOD
                
                if end_plus_one < n:
                    # To "divide" by v, we multiply by its modular inverse.
                    # This is necessary to avoid floating point errors and keep numbers small.
                    inv_v = pow(v, MOD - 2, MOD)
                    p[end_plus_one] = (p[end_plus_one] * inv_v) % MOD

            # Accumulate the multipliers down each of the 'k' independent lanes.
            # An element at index 'i' inherits its multiplier from the previous
            # element in its lane, which is at index 'i-k'.
            for i in range(k, n):
                p[i] = (p[i] * p[i - k]) % MOD
            
            # Now that the multiplier array 'p' is fully built for this 'k',
            # apply it to the main nums array.
            for i in range(n):
                nums[i] = (nums[i] * p[i]) % MOD
        
        # PART 3: FINAL CALCULATION
        # After all heavy and light queries have been applied, calculate the final XOR sum.
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        return xor_sum
