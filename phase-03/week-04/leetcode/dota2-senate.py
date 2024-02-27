class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # we keep track of the number of banned senators for each party
        # and we re-append the current senator only if the number of senators banned
        # from his party is 0
        q = deque(senate)
        r, d = senate.count("R"), senate.count("D")
        banned_r, banned_d = 0, 0

        while q and r > 0 and d > 0:
            a = q.popleft()
            if a == "R":
                if banned_r > 0:
                    banned_r -= 1
                else:
                    banned_d += 1
                    d -= 1
                    q.append(a)
            elif a == "D":
                if banned_d > 0:
                    banned_d -= 1
                else:
                    banned_r += 1
                    r -= 1
                    q.append(a)
        
        return "Radiant" if r > 0 else "Dire"
