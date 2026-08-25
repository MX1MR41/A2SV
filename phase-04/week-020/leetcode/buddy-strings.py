class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False

        diff = []
        i = 0
        while i < len(s):
            if s[i] != goal[i]:
                diff.append(i)

                if len(diff) > 2: return False

            i += 1

        if not diff:
            cnt = Counter(s)
            for i, j in cnt.items():
                if j >= 2: return True

        if len(diff) != 2: return False
        a, b = diff
        if s[a] == goal[b] and s[b] == goal[a]: return True
        else: return False


            
        

        
