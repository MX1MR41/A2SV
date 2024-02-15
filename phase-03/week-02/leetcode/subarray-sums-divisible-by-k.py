class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # we calculate prefix sum as we go and each time, 
        # we check to see if we have seen a prefix sum whom if subtracted
        # from the current prefix sum, would make it divisble by k
        # the formula is if (a - b) % k == 0 then a % k == b % k
        # meaning if two numbers a and b have the same remainder when divided by a certain number k
        # then deducting one of them from the other would make them divisble by k
        seen = defaultdict(int) # stores seen prefix sums
        seen[0] = 1 # initialize with prefix sum zero since before we start the array, we have a sum of 0
        res = 0
        pre = 0 # prefix sum counter
        for i in nums:
            pre += i
            extra_sum = pre % k # the number that would make pre divisble by k
            # think of it cyclically; if the remainder of dividing a certain number
            # becomes the same as some remainder we saw with a previous number, 
            # that means that the cycle has restatrted and
            # and that the range between those two numbers was divisible by k
            if extra_sum in seen:
                res += seen[extra_sum] # if we have x such numbers, then there are x such valid possible deduction combinations
                seen[extra_sum] += 1 # doing this instead of seen[pre] += 1, will yeild better effects
                # because you'll still store the remainder but choosing the smaller extra_sum would ensure
                # you wont miss any such subarrays in the future
            else:
                seen[extra_sum] += 1

        return res
        