class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # a custom function that will check if the occurence of each element 
        # in the first counnter is less than or equal to its occurence in 
        # the second counter; meaning, if the all the letters of the word represented
        # by the second counter are included in the second counter
        def compare(countert, counters):
            for i in countert:
                if counters[i] < countert[i]:
                    return False

            else:
                return True

        flag = False # to validate presence of a single valid case i.e. t contained in s
        n, res, l = len(s), s, 0
        tcnt, scnt = Counter(t), defaultdict(int)

        for r in range(n):
            i = s[r]
            scnt[i] += 1

            while l <= r and compare(tcnt, scnt):
                flag = True
                curr = s[l:r+1]
                if len(curr) < len(res):
                    res = curr
                lchar = s[l]
                if scnt[lchar] > 0:
                    scnt[lchar] -=1
                l += 1

        return res if flag else ""

        