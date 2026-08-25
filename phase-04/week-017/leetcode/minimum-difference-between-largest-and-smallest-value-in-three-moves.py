class Solution:
    def minDifference(self, nums: List[int]) -> int:

	    # if the list is sorted then the  
        # the min of the first 3 numbers should change it to being as close as possible to the max
		# or the min of first 2 numbers should change and max of last number should be second last...
		# basically, we need to check which of the following changes gives me least diff - 
		# is changing n[0], n[1], n[2] to n[3] 
		# or changing n[0],n[1] to n[2] and n[-1] to n[-2], 
		# or n[0] to n[1] and n[-1],n[-2] to n[-3] 
		# or n[-1],n[-2],n[-3] to n[-4] giving the smallest diff 
		# when i sort the list, there really aren't any other combos we can get to by changing any 3 numbers really which would 
		# bring the diff between min and max down
		# if there are 4 or less numbers then difference will always be zero no need to check anything at all.

        if len(nums) <= 4:
            return 0

        nums.sort()

        return min( (nums[-1]-nums[3]), (nums[-2]-nums[2]), (nums[-3]-nums[1]), (nums[-4]-nums[0]) )
