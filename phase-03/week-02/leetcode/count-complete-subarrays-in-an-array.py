class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        curr = defaultdict(int)
        cnt = Counter(nums)
        distinct = len(cnt)

        n = len(nums)
        l = 0
        res = 0

        for r in range(n):
            rnum = nums[r]
            curr[rnum] += 1
            

            while len(curr) == distinct:
                res += n - r
                lnum = nums[l]
                curr[lnum] -= 1
                
                if curr[lnum] == 0:
                    curr.pop(lnum)

                l += 1
    

        return res


        


        