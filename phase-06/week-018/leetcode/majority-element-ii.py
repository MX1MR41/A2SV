class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # voting method where the majority candidates would outvote other candidates
        cand1 = cand2 = None
        vote1 = vote2 = 0

        for i in nums:
            if i == cand1:
                vote1 += 1
            elif i == cand2:
                vote2 += 1

            elif vote1 == 0:
                cand1, vote1 = i, 1

            elif vote2 == 0:
                cand2, vote2 = i, 1
            

            else:
                vote1 -= 1
                vote2 -= 1

        return [c for c in (cand1, cand2) if nums.count(c) > len(nums)//3]

        
