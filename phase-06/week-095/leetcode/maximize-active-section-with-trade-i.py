class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # sliding window + prefix sum
        # for every index i, precompute the following:
        # 1) the number of contiguous zeros to the left of i
        # 2) the number of contiguous zeros to the right of i
        # 3) the total number of ones to the left and right of i
        # then use that data to find the answer
        res = s.count("1")


        pre_0 = []
        pre_1 = []
        p0 = p1 = 0
        for i in s:
            pre_0.append(p0)
            pre_1.append(p1)
            if i == "0":
                p0 += 1
            else:
                p1 += 1
                p0 = 0 # break the zero count since we only want contiguous

        suf_0 = []
        suf_1 = []
        s0 = s1 = 0
        for i in s[::-1]:
            suf_0.append(s0)
            suf_1.append(s1)
            if i == "0":
                s0 += 1
            else:
                s1 += 1
                s0 = 0

        suf_0.reverse()
        suf_1.reverse()

        n = len(s)
        l = 0
        for r in range(n):
            if s[r] == "1":
                continue
            
            if l < r and l > 0:
                left_0 = pre_0[l]
                right_0 = suf_0[r - 1]

                l_bound = l - left_0
                r_bound = r - 1 + right_0

                left_1 = pre_1[l_bound]
                right_1 = suf_1[r_bound]

                curr = r - l + left_0 + right_0 + left_1 + right_1
                res = max(res, curr)

            l = r + 1
        
        return res
                

        

        
