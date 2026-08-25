class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def tmp():
            return -1

        stk = []
        lookup = defaultdict(tmp)
        for i,x in enumerate(nums2):
            while stk and stk[-1][1] < x:
                lookup[stk.pop()[1]] = x

            stk.append((i,x))

        res = [lookup[x] for x in nums1]
        
        return res