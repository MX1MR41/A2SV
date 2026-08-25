class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # dynamic programming
        

        n = len(bits)
        one = [False] * n
        two = [False] * n

        if bits[0] == 0:
            one[0] = True

        for i in range(1, n):
            if bits[i] == 0 and (one[i - 1] or two[i - 1]):
                one[i] = True

            if (
                ((bits[i] == 0 and bits[i - 1] == 1) or (bits[i] == bits[i - 1] == 1))
                and (i == 1 or one[i - 2] or two[i - 2])
            ):
                two[i] = True


        return one[-1]
        
