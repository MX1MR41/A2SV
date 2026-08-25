class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # dp + math
        # if arr[i+2] % arr[i+1] == arr[i+1] % arr[i] == 0, then arr[i+2] % arr[i] == 0
        # we need to find the longest subsequence where every consecutive element 
        # modularizes to 0, i.e. for every i in range(len(res)-1), res[i+1] % res[i] == 0
        # create a dp array that will store for every number the maximum length of a subsequence
        # ending by that number. For every nnumber, try each number before it to see which can
        # divide it and if so which gives the maximum subsequence length when appended by number
        # also keep track of the best previous number for every number, to help reconstruct
        # the longest subsequence following number to prev number 
        
        if len(nums) == 1:
            return nums

        nums.sort()

        n = len(nums)
        dp = [1] * n
        start = 0
        last_max_dp = 0
        prev = defaultdict(int)
        for i in range(1, n):
            a = nums[i]
            maxx = 0
            for j in range(i):
                b = nums[j]
                if not a % b:
                    if dp[j] >= maxx:
                        prev[a] = b
                        maxx = dp[j]

            dp[i] += maxx
            if dp[i] >= last_max_dp:
                start = a
                last_max_dp = dp[i]


        res = []
        while start > 0:
            res.append(start)
            start = prev[start]

        return res

        
