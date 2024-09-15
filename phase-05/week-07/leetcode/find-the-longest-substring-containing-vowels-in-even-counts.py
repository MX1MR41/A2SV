class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # bit manip + prefix sum
        # if a certain string contains an even number of vowels,
        # they would cancel out when XOR-ed leaving a total XOR of zero.
        # create a an XOR prefix then find the first and last indices
        # of each XOR in the prefix whose difference could make 0

        vs = set(["a","e","i","o","u"])
        n = len(s)
        pre = [0] # case when the substring might start from first index
        p = 0



        for i in range(n):
            v = s[i]
            if v in vs:
                p ^= ord(v)

            pre.append(p)


        first = defaultdict(lambda: float("inf"))
        last = defaultdict(int)

        for i in range(n+1):
            j = pre[i]
            first[j] = min(first[j], i)
            last[j] = max(last[j], i)


        ans = 0

        for i in first:
            ans = max(ans, last[i] - first[i])

        return ans

        
