class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # two pointers
        # traverse the strings simultaneously with a pointer each
        # Skip _'s. If L is found, traverse in the target to find next L. If found and
        # that found L happens to be to the right, return False since we can't move to it
        # similar logic with R

        # preliminary check and elimination
        if start.count("L") != target.count("L") or start.count("R") != target.count("R"):
            return False

        i = j = 0

        n, m = len(start), len(target)
        while i < n:
            #skipping _'s
            while i < n and start[i] == "_":
                i += 1
            
            # finished the string with no matching required
            if i >= n:
                break

            # traverse the target to find the next non-_ character
            while j < m and target[j] == "_":
                j += 1

            # if we have run out or the found character doesn't match
            if j >= m or start[i] != target[j]:
                return False

            # if the L found in target is to the right
            if start[i] == "L" and j > i:
                return False
            # if the R found in target is to the left
            if start[i] == "R" and j < i:
                return False

            i += 1
            j += 1


        return True

