class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # the approach is to use a double loop coupled with a two pointers method
        # sorting the array is necessary so we can greedily calculate the count
        # for every num starting from the right(the biggest), we use two pointers
        # at the start and just before the current number
        # if those three nums (the current, the left and right) are valid,
        # then all the numbers in between the left and right are also valid 
        # i.e the combinations of the current num, the right num and all the nums
        # starting from the left to just before the right pointer
        res = 0 
        n = len(nums)
        nums.sort() 

        for i in reversed(range(1,n)):
            l, r = 0, i - 1

            while l < r:
                a, b, c = nums[l], nums[r], nums[i]

                if a + b > c:
                    res += r - l
                    r -= 1

                else:
                    l += 1


        return res
        