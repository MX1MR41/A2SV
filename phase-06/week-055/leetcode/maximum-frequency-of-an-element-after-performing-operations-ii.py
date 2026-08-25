class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # prefix sum with hashmap + binary search
        # since num could reach 10^9, we can't use an array to build a prefix sum
        # instead we'll use a hasmap to build a compressed prefix sum
        # part 1: iterate over every num in nums and use its original frequency, 
        # its prefix sum bracket and numOperations to see how big its frequency could get
        # part 2: iterate over the prefix sum brackets and use the freqs and numOps to 
        # see how big its frequency could get


        prefix = defaultdict(int)
        for num in nums:
            start, end = num - k, num + k
            prefix[start] += 1
            prefix[end + 1] -= 1

        flat_prefix = [[num, freq] for num, freq in sorted(prefix.items())]

        for i in range(1, len(flat_prefix)):
            flat_prefix[i][1] += flat_prefix[i - 1][1]



        res = 0

        count = Counter(nums)

        for num in nums:
            total = count[num] # initial frequency of num
            ind = -1 # the bracket in which num belongs to from the prefix sum array
            # binary search to find correct ind
            l, r = 0, len(flat_prefix) - 1
            while l <= r:
                mid = (l + r) // 2
                if flat_prefix[mid][0] <= num:
                    ind = mid
                    l = mid + 1
                else:
                    r = mid - 1

            # count of other nums on whom we can apply operations to turn them to num
            # exclude the original frequency of num because we have already counted it
            extras = max(0, flat_prefix[ind][1] - count[num])
            
            total += min(extras, numOperations)

            res = max(res, total)


        for num, freq in flat_prefix:
            extras = freq

            total = min(extras, numOperations)

            res = max(res, total)

        return res
