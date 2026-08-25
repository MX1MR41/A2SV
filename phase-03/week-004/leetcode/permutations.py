class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def permute(arr, per):
            if len(per) == len(arr):
                ans.append(per[:])
                return

            for i in arr: # try all possible permutation with nums other than the current
                if i not in per:
                    per.append(i)
                    # recursively explore other permutations with the current i
                    permute(arr, per)
                    # after the recursive call returns, we pop i and try other nums
                    per.pop()

        permute(nums,[])

        return ans