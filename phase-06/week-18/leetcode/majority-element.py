class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # voting method
        # initialize a variable to hold a possible candidate and its count
        # increase that count if we see it again, decrement it if we see another
        # at the end the candidate should be the majority element
        vote = 1
        cand = nums[0]
        for i in nums[1:]:
            if cand != i:
                vote -= 1
                if vote == 0:
                    cand = i
                    vote = 1

            else:
                vote += 1

        return cand
        
