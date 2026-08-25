class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # approach works by recursively checking for the optimal choice 
        # in the next state, basically seeing one step ahead at a time at every state
        # until we can't see ahead anymore. 
        l, r = 0 , len(nums) - 1

        def dfs(left, right):
            # base case, the array isnt vlid
            if left > right:
                return 0, 0
            
            # the cumulative sum of optimal choices for player 1 and the next choice
            curr1, nxt1 = dfs(left+1, right)
            # the cumulative sum of optimal choices for player 2 and the next choice
            curr2, nxt2 = dfs(left, right-1)
                        
            # if the choice of the first element is optimal considering
            # the next step ahead
            if nums[left] + nxt1 > nums[right] + nxt2:
                return nums[left] + nxt1, curr1
            
            # the opposite
            return nums[right] + nxt2, curr2
        
        p1, p2 = dfs(l, r)
        
        return p1 >= p2