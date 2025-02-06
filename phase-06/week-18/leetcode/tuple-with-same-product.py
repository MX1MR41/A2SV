class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        tups = defaultdict(set)
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i != j and nums[i] != nums[j]:
                    prod = nums[i]*nums[j]
                    tups[prod].add(tuple(sorted([nums[i], nums[j]])))

        

        res = 0
        for prod, tup in tups.items():
            abcds = list(tup)
            
            m = len(abcds)
            for i in range(m):
                for j in range(i + 1, m):
                    uni = set(list(abcds[i]) + list(abcds[j]))
                    if len(uni) == 4:
                        res += 8

        return res
        
