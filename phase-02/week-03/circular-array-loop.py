class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def dest(i):
            return (i + nums[i]) % n
        
        n = len(nums)
        for i in range(n):
            if nums[i] == 0: 
                continue
            fast = slow = i
    
            while nums[fast] * nums[dest(fast)] > 0 and \
                  nums[dest(fast)] * nums[dest(dest(fast))] > 0:
                fast = dest(dest(fast))
                slow = dest(slow)
                if slow == fast:
                    if slow == dest(slow):
                        break 
                    return True
            
            slow = i
            while slow * nums[dest(slow)] > 0:
                next_slow = dest(slow) 
                nums[slow] = 0 
                slow = next_slow 
            
        return False