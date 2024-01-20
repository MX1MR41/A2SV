class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot = 1
        z, n = 0, len(nums)
        flag = False
        for i in nums:
            if not i:
                flag = True
                z += 1
            else:
                tot *= i


        res = []

        for i in nums:
            if not i:
                if z > 1:
                    res.append(0)
                else:
                    res.append(tot)
            else:
                if flag:
                    res.append(0)
                else:
                    res.append(tot//i)

        return res
        