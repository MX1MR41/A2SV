class Solution:
    def smallestNumber(self, num: int) -> int:
        ans, num = "", str(num)
        if num == '0':
            return 0
        if num[0] != '-':
            zeros, nums = "", []
            for i in num:
                if i == '0':
                    zeros += '0'
                else:
                    nums.append(i)
            nums.sort()
            ans += nums[0] + zeros + "".join(nums[1:])
            return int(ans)
        else:
            zeros, nums = "", []
            for i in num[1:]:
                if i == '0':
                    zeros += '0'
                else:
                    nums.append(i)
            nums.sort(reverse = True)
            ans += "".join(nums) + zeros
            return 0 - int(ans)

        



        