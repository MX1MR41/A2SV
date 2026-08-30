class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minn = [float("inf"), -1]
        maxx = [float("-inf"), -1]
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if num > maxx[0]:
                maxx = [num, i]

            if num < minn[0]:
                minn = [num, i]


        start = -1
        end = n
        ind1 = minn[1]
        ind2 = maxx[1]
        res = 0
        if min(ind1 - start, end - ind1) <= min(ind2 - start, end - ind2):
            if ind1 - start <= end - ind1:
                res += ind1 - start
                start = ind1
            else:
                res += end - ind1
                end = ind1

            if ind2 - start <= end - ind2:
                res += ind2 - start
                start = ind2
            else:
                res += end - ind2
                end = ind2

        else:
            if ind2 - start <= end - ind2:
                res += ind2 - start
                start = ind2
            else:
                res += end - ind2
                end = ind2

            if ind1 - start <= end - ind1:
                res += ind1 - start
                start = ind1
            else:
                res += end - ind1
                end = ind1

        return res

        
