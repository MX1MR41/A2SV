class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # two pointers
        
        def addtores(x, xv):
            if not res or (res and res[-1][0] != x):
                res.append([x, xv])
            else:
                res[-1][1] += xv


        res = []
        m, n = len(nums1), len(nums2)
        i = j = 0
        while i < m and j < n:
            a, av = nums1[i]
            b, bv = nums2[j]
            if a == b:
                addtores(a, av + bv)
                i += 1
                j += 1

            elif a < b:
                addtores(a, av)
                i += 1
            else:
                addtores(b, bv)
                j += 1

        while i < m:
            addtores(*nums1[i])
            i += 1

        while j < n:
            addtores(*nums2[j])
            j += 1

        return res
  
        
