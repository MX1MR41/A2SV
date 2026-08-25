class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorting + two pointers
        # for every num, we do a two pointers search over the rest of the array
        # to find valid choices
        
        nums.sort()
        n = len(nums)
        triplets = set()
        for i in range(n):
            a = nums[i]
            need = 0 - a
            left, right = i + 1, n - 1

            while left < right:
                b, c = nums[left], nums[right]
                two_sum = b + c
                if two_sum == need:
                    triplets.add(tuple([a, b, c]))
                    left += 1
                    right -= 1

                if two_sum < need:
                    left += 1

                if two_sum > need:
                    right -= 1

        return list(triplets)

        
