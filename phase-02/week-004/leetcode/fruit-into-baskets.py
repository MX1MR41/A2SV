class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        # a set to hold the type of fruits observed so far
        # and a dictionary to count the frequency of each type
        seen, cnt = set(), defaultdict(int)
        res = l = 0 # the result variable and the left pointer of the sliding window

        for r in range(n): # right pointer of the sliding window
            fr = fruits[r] # the current fruit
            if fr not in seen:
                seen.add(fr)

            cnt[fr] += 1
            # since we can only carry two types of fruits, when the seen fruits become three,
            # we shrink the left pointer of the window while discarding fruits from the left
            # until we are carrying only two types
            while len(seen) > 2: 
                fl = fruits[l] 
                if cnt[fl] > 0:
                    cnt[fl] -= 1
                    l += 1
                if cnt[fl] == 0:
                    seen.discard(fl)

            res = max(res, r - l + 1)

        return res
        