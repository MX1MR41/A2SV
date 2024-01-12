class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen, n = set(), len(nums)
        l, r  = 0, 0
        res = curr = 0

        for r in range(n):
            num = nums[r] # the current number

            if num in seen:
                # shrinking the window from the left until we find the past occurence of num
                while nums[l] != num:
                    seen.discard(nums[l])
                    curr -= nums[l]
                    l += 1
                # we found the past occurence of num, so now we move the pointer beyond it
                # so the sliding window contains only the unique items
                seen.discard(nums[l])
                curr -= nums[l]
                l += 1

            curr += num
            seen.add(num)
            res = max(curr,res)

        return res

        