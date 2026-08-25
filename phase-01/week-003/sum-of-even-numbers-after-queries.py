class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = sum(n for n in nums if not n % 2)
        result = []

        for i in queries:
            num, index = nums[i[1]], i[1]

            if not num % 2:
                ans -= num

            nums[index] += i[0]

            if not nums[index] % 2:
                ans += nums[index]

            result.append(ans)

        return result
