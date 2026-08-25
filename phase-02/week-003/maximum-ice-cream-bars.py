class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        m = max(costs)
        count = [0] * (m+1) # counting sort array
        ice = 0

        for i in costs: # populate count sort
            count[i] += 1

        for j in range(m+1): # traverse count sort
            if coins <= 0: # if kid runs out of coins, then break
                break

            c = count[j] # the number of icecreams with cost j

            while c > 0: # check if the kid still has coins after buying one by one
                coins -= j
                if coins >= 0:
                    ice += 1

                c -= 1

        return ice