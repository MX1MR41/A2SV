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
