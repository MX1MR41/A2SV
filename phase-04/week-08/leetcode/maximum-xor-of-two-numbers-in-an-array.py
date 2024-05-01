class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # the solution works by coupling bit manipulation with a greedy approach
        # we need to find a number such that is has more ones to the right than all possiblities
        # we start from the rightmost bit position and check if it is possible for us to 
        # flip it on (if so we do and if not we don't) until the leftmost position
        # by the time we have finished, we get a number such that all of its leftmost bits 
        # have been flipped on if there were two numbers whose xor could flip it on

        res = mask = 0 
        n = max(nums).bit_length() # the index of the leftmost possible bit of our answer

        # we don't start from the leftmost bit because we have no way of knowing
        # what the maximum possible prefix of our answer could have been
        # instead we start from the rightmost and build up our result as a prefix
        for i in reversed(range(n)):
            # the maximum possible prefix (all 1's) for i (eg. if i = 2 then mask = ...11100) 
            mask = mask | (1 << i)
            # the maximum possible answer so far after all the prefix bits
            # that could've been flipped on have been done so
            curr = res | (1 << i)


            prefixes = set()
            for num in nums:
                # AND-ing the number with mask (which has all bits upto i as 1) yields
                # a possible maximum prefix 
                pref = num & mask
                prefixes.add(pref)
          
            # now we use a method similar to the Two-Sum problem where we validate by checking
            # to see if a certain complementary value to our current value is present
            for prefix in prefixes:
                twin = prefix ^ curr
                # if A ^ B = C then B ^ C = A 
                # if twin exists in the possible prefixes, then it is possible 
                # to obtain curr (the maximum possible prefix upto i) by XOR-ing them
                if twin in prefixes:
                    res = curr
                    break 
                  
        return res
