class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # same as https://leetcode.com/problems/hand-of-straights/
        if len(nums) % k: return False
        cnt = Counter(nums)
        heapify(nums)
        
        while nums:
            while nums and not cnt[nums[0]]:
                heappop(nums)
            
            if nums:
                num = heappop(nums)
            else:
                break
            
            curr = num + 1

            for _ in range(k - 1):
                if cnt[curr]:
                    cnt[curr] -= 1
                    curr += 1
                else:
                    return False
            
            cnt[num] -= 1
            if cnt[num]:
                heappush(nums, num)

        return True
