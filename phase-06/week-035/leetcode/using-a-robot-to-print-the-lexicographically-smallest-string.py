class Solution:
    def robotWithString(self, s: str) -> str:
        # stack + prefix minimum + suffix minimum
        # For some letter s[i], it would be best to append it to our result if and only if
        # we are sure we won't see any letter in the future that are smaller than it.
        # If it doesn't happen to be such a letter, we append it to t, because we are 
        # anticipating a smaller letter in the future.
        # Another thing to be aware of is that if s[i] happens to be the smallest letter
        # from all the letters starting from it to the end, we need to check the letters
        # we stored in t before directly appending s[i] to our result. That is because 
        # there might be a letter in t which is smaller than s[i] and needs to be appended
        # to the result before appending s[i].
        # We can keep track of the smallest suffix letters and prefix letters to help us
        # simulate this process.

        n = len(s)

        suf_min = ["{"] * n # initilaizing with { instead of float("inf") since { > z
        suf_min[-1] = s[-1]

        for i in range(n - 2, -1, -1):
            suf_min[i] = min(suf_min[i + 1], s[i])

        pre_min = ["{"]

      

        t = []
        res = []
        for i in range(n):
            letter = s[i]

            
            while pre_min[-1] <= letter and pre_min[-1] <= suf_min[i]:
                res.append(pre_min.pop())
                t.pop()


            if letter <= suf_min[i]:
                res.append(letter)
            else:
                t.append(letter)
                pre_min.append(letter)


        return "".join(res + t[::-1])
        
