class Solution:
    def processStr(self, s: str, k: int) -> str:
        # just rewind time and iterate backwards
        # first construct an array to store the size of the string after each step
        # then move backwards while doing the appropriate transformations to k until the kth letter

        size = []
        curr = 0
        for i in s:
            if i == "*":
                if curr > 0:
                    curr -= 1
            elif i == "#":
                curr *= 2
            elif i == "%":
                pass
            else:
                curr += 1

            size.append(curr)


        # out of bounds
        if k >= size[-1]:
            return "."

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "*":
                pass

            elif s[i] == "#":
                # if k is in the seond half then bring it to the first half
                # because it is a mirror of the first half
                curr = size[i]
                mid = curr // 2
                if k >= mid:
                    k -= mid

            elif s[i] == "%":
                # if k was x steps from the left, then bring it to x steps from the right
                curr = size[i]
                k = curr - 1 - k

            else:
                # if this letter was the one that cause the size to become k + 1
                # then we found the kth letter
                if size[i] - 1 == k:
                    return s[i]

        return "."

