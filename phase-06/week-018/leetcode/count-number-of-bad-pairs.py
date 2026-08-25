class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # j - i = n[j] - n[i] ==> n[i] - i = n[j] - j
        # so for every index j, whose value = n[j] - j,
        # you need to find out how many previous indices j don't have 
        # n[i] - i equal to value
        
        count = defaultdict(int)
        n = len(nums)

        pairs = 0

        for i in range(n):
            curr = nums[i] - i
            curr_count = count[curr]
            pairs += i - curr_count

            count[curr] += 1

        return pairs

        
