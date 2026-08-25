class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        m = max(nums)
        d = {} # map to hold nums mapped to how many nums smaller than them
        csort = [0] * (m+1) # counting sort
        pre = 0 # prefix sum variable

        for i in range(len(nums)):
            csort[nums[i]] += 1

        print(csort)

        # for every num, we map it to the total sum of freqs in csort less upto that index
        for ind, x in enumerate(csort):
            d[ind] = pre
            pre += x

        for j in range(len(nums)):
            nums[j] = d[nums[j]]

        return nums
        
        