class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # sorting the array ensures that subsets are generated in a predictable order.
        # This predictable order helps in avoiding duplicate subsets efficiently
        nums.sort()  
        res = []

        def sub(start, comb):
            res.append(comb[:])  

            # iterating from the start index will prune away all other possibilities
            # of generating subsets which we have already seen.
            # and the array being sorted helps with avoiding repetitious generation
            for i in range(start, len(nums)):
                comb.append(nums[i])
                sub(i + 1, comb)  
                comb.pop()

        sub(0, [])
        return res