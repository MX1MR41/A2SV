class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill) - 1
        tot, chem = skill[r] + skill[l] , 0

        while l < r:
            curr = skill[r] + skill[l]
            if curr != tot:
                return -1
            
            chem += skill[l] * skill[r]
            l += 1
            r -= 1

        return chem

        