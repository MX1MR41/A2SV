class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # monotonic queue + sliding window
        # we slide a window over our array while keeping track of the largest and smallest
        # nums in our window using monotonic queues, one increasing other decreasing
        maxque, minque = deque(), deque()
        ans = 0
        n = len(nums)
        left = 0
        for right in range(n):
            curr = nums[right]

            # put the current number in its appropriate places in both queues
            while maxque and maxque[-1][0] < curr:
                maxque.pop()
            maxque.append((curr, right))

            while minque and minque[-1][0] > curr:
                minque.pop()
            minque.append((curr, right))
            
            # while our current window is invalid, we keep shrinking our window
            # invalidity condition: abs(smallest - biggest) > 2
            while minque and maxque and abs(minque[0][0] - maxque[0][0]) > 2 and left < right:
                left += 1

                # from the front of both our queues, we pop any element that is located 
                # outside the window we just shrunk
                # it is guaranteed that every element is in increasing order of indices
                # so we can prune the outsiders easily
                while minque and minque[0][1] < left:
                    minque.popleft()

                while maxque and maxque[0][1] < left:
                    maxque.popleft()

            # adding a new element to a valid window means we can create a subarray with it
            # and every other subarray (which would be the number of elements before)
            # if len(prev_window) == n, adding one more element gives us n new subarrays
            ans += right - left + 1


        return ans
        
