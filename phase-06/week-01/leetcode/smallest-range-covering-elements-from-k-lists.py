class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # heap
        # Store an element from every group into a heap then keep replacing by a group-mate
        # and calculating the result.
        # Start from the first element of every group and push into heap along with their group 
        # and index number (row, col).
        # From the first nums, store the max one. And at all time when replacing a number
        # update the max.

        k = len(nums)
        heap = []  
        largest = float("-inf")

        
        for i in range(k):
            row, col = i, 0
            smallest = nums[row][col]
            heappush(heap, (smallest, row, col))
            largest = max(largest, smallest)

        ans = [0, float("inf")]
        while len(heap) == k:
            smallest, row, col = heappop(heap)

            if largest - smallest < ans[1] - ans[0] or (largest - smallest == ans[1] - ans[0] and smallest < ans[0]):
                ans = [smallest, largest]

            next_index = col + 1
            if next_index < len(nums[row]):
                next_num = nums[row][next_index]
                largest = max(largest, next_num)
                heappush(heap, (next_num, row, next_index))

        return ans
            


        
        

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Sliding window + prefix sum
        # Convert each list into a set and store in a hashmap with their indices as keys.
        # Create a sorted list of all the unique numbers.
        # Create a prefix sum for each set where the sum is the 
        # number of member elements of that set seen so far.
        # Slide a window that shrinks as long as there is at least a member from each set,
        # expand it if even a single set doesn't have a member in the window

        k = len(nums)
        lists = defaultdict(set)
        for i in range(k):
            lists[i] = set(nums[i])

        num = []
        for n in nums:
            num += n

        num = list(set(num)) # convert to a list of unique elements
        num.sort()
        n = len(num)

        prefix = defaultdict(lambda: [0]) # 0-padding for prefix sum
        for i in range(k):
            p = 0
            for j in num:
                if j in lists[i]:
                    p += 1

                prefix[i].append(p)


        # counts the number of sets that have at least a member each between l and r
        def count(l, r):
            cnt = 0
            for i in prefix:

                if prefix[i][r] - prefix[i][l]:
                    cnt += 1

            return cnt


        num = [0] + num
        ans = [0, float("inf")]

        l = 0

        for r in range(n+1):
            while count(l, r) >= k:
                a, b = num[l + 1], num[r]
                if b - a < ans[1] - ans[0] or (b - a == ans[1] - ans[0] and a < ans[0]):
                    ans = [a, b]
                l += 1

        return ans
