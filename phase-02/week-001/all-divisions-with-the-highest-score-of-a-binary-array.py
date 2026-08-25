class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        left, right = Counter(nums[:0]), Counter(nums)

        big = 0

        inds = defaultdict(list)

        

        i = 0
        while i < len(nums):

            div = left[0] + right[1]
            inds[div].append(i)
            big = max(div, big)

            
            if nums[i]:
                right[1] -= 1
            else:
                left[0] += 1

            i += 1

        big = max(big, right[0])

        inds[right[0]].append(len(nums))


        return inds[big]



        