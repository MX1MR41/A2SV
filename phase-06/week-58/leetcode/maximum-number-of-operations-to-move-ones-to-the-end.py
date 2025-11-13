class Solution:
    def maxOperations(self, s: str) -> int:
        # prefix sum
        # for each 1 in the string, the number of operations required to bring
        # it to the end of the string is the same as the number of 0 substrings
        # in the string. That is because the 1 will definitely have to cross 
        # those individual 0 substrings before it could reach the end
        # so, first we compress the string so that consecutive 0s become one 0
        # to help with computation. Then build a suffix sum array where the sum
        # is the number of zero substrings to the right
        # for each 1 count the number of 0 subs to the right as number of ops

        new_s = []
        for i in s:
            if not new_s or i == "1":
                new_s.append(i)
                continue

            if new_s[-1] == i:
                continue
            else:
                new_s.append(i)
        
        s = new_s
        n = len(s)


        zeros_suf = [0] * n
        zeros = 0
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                zeros += 1

            zeros_suf[i] = zeros


        ops = 0
        for i in range(n - 1):
            if s[i] == "1":
                ops += zeros_suf[i]


        return ops





        
