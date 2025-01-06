class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # prefix sum + suffix sum
        # let our indices be [a,b,c,d,e] and let us assume they are all "1", let us solve for c
        # from the left side => abs(a - c) + abs(b - c) => c - a + c - b => 2*c - (a + b)
        # for index i from the left the total will be i * (no of 1 indices) - (sum of indices)
        # and from the right it will be ther reverse i.e -(i*(no) - (sum))
        n = len(boxes)
        prefix = []
        pre_cnt = pre = 0
        for i in range(n):
            prefix.append((pre_cnt, pre))
            if boxes[i] == "1":
                pre_cnt += 1
                pre += i

        suffix = []
        suff_cnt = suff = 0

        for i in range(n - 1, -1, -1):
            suffix.append((suff_cnt, suff))
            if boxes[i] == "1":
                suff_cnt += 1
                suff += i

        suffix.reverse()

        ans = [0] * n
        for i in range(n):
            pre_cnt, pre = prefix[i]
            suff_cnt, suff = suffix[i]

            ans[i] = (i * pre_cnt) - pre - (i * suff_cnt) + suff

        return ans
