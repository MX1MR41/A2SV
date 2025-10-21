class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # sorting + binary search
        # we try every possible number to see if it could be the number that could yield
        # the maximum frequency out of all numbers
        # after we sort the nums, we iterate for every num in the range
        # and we need to find out how many numbers can be modified
        # i.e. operated on by a delta in [-k, k] to become num. So finding the left bound
        # of num - k and right bound of num + k in the sorted array
        # once we do that, we can change numOperations amount of them into num

        nums.sort()
        m = nums[-1]

        count = Counter(nums)
        res = 0
        
        for num in range(m + k + 1):
            total = count[num]

            l = bisect.bisect_left(nums, num - k)
            r = bisect.bisect_right(nums, num + k)

            other_nums = r - l - count[num] # deduct for num iytself

            total += max(0, min(other_nums, numOperations))
            res = max(res, total)

        return res

