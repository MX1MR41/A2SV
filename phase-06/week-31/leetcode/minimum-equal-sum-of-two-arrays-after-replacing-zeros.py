class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # greedy
        # if we have zeros in both arrays, we can use them to make them sums meet somewhere
        # forward on the number line, so we take the maximum of the minimum such jumps of
        # either sum, where the minimum jump of a sum would be sum + zeros naking all zeros = 1

        sum1 = sum(nums1)
        sum2 = sum(nums2)

        z1 = nums1.count(0)
        z2 = nums2.count(0)

        if z1 == 0 and z2 != 0:
            if sum2 + z2 <= sum1:
                return sum1
            else:
                return -1

        if z1 != 0 and z2 == 0:
            if sum1 + z1 <= sum2:
                return sum2
            else:
                return -1

        if z1 == z2 == 0:
            if sum1 == sum2:
                return sum1
            else:
                return -1

        return max(sum1 + z1, sum2 + z2) 
