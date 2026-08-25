class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        indices = defaultdict(list)
        for i in range(n):
            letter = s[i]
            indices[letter].append(i)

        total = 0
        for i, j in indices.items():
            m = len(j)
            can_delete = m - 1
            times = can_delete//2
            total += m - times*2

        return total
        
