class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # solved the problem by storing the already seen rabbits and cross-checking with that.
        # each time we meet a rabbit who has the same number of rabbits with similar color as an already seen rabbit has,
        # we deduct from the value in the already seen number of rabbits who said that they have the same number as the current one
        # it could be a different color for all we know, but we can greedily finish our calculations like this
        seen = defaultdict(int) 
        rabbits = 0
        for i in answers:
            if not seen[i]: 
                seen[i] += i
                rabbits += i + 1
            else:
                seen[i] -= 1
            

        return rabbits


        