class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        arr = sorted(nums)
        ans = 0
        c = Counter(nums)
        s = sorted(list(set(arr)))
        print(s)
        for i in range(len(c) - 1): # it won't reach the smallest element
            M = s.pop() # get the largest element
            ans += c[M] # increment ans by frequency of that element
            c[s[-1]] += c[M] # increment the freq of next largest 

        return ans

            