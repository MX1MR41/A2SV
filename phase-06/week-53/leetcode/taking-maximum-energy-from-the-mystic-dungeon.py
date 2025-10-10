class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # dp
        # start from the last k wizards and move backwards summing up the energies
        # since starting at index i, will eventually take you to i+k, i+2k, i+3k...
        # we can cover all such indices by starting from the last i+xk 
        # then going to i+(x-1)k, i+(x-2)k, ... i+2k, i+k, i
        # that way we will have computed all the possible energies we could get if we start
        # from any of theses indices
        n = len(energy)
        for i in range(n - 1, n - k - 1, -1):
            
            for j in range(i - k, -1, -k):
                energy[j] += energy[j + k]

        return max(energy)
        
