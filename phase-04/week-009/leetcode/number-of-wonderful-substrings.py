class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # prefix xor 
        # represent the parity of frequency of letter in a bitmask of length 10 (a-j)
        # each iteration we xor the letter's bit with the bitmask
        # and keep toggling the bits one by one and checking to see if 
        # the toggled bitmask existed as a prefix, if so add its occurence to our result
        n = len(word)
        pre = defaultdict(int)
        pre[0] += 1

        mask = res = 0

        for i in range(n):
            letter = word[i]
            mask ^= 1 << (ord(letter) - 97)
            # if the mask becomes 0 (all even), we add the number of even prefixes
            # to our result because un-xor-ing them would give us even too
            res += pre[mask]

            for j in range(10):
                new_mask = mask ^ (1 << j)
                res += pre[new_mask]

            pre[mask] += 1

        return res
