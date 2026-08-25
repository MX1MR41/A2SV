class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # sliding window + monotonic queue
        # use a sliding window which is actually a monotonic queue
        # store the element with their indices
        # at every slide, first eliminate all elements which should be out of the window from left 
        # it is guaranteed all element in the queue are stored in appearance order
        que = deque()
        for i in range(k):
            curr = nums[i]
            while que and que[-1][0] < curr:
                que.pop()

            que.append((curr, i))

        ans = [que[0][0]]

        for i in range(k, len(nums)):
            left = i - k
            curr = nums[i]
            while que and que[0][1] <= left:
                que.popleft()
            while que and que[-1][0] < curr:
                que.pop()

            que.append((curr, i))

            ans.append(que[0][0])

        return ans

            




        
        
