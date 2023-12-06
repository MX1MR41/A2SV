class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        steps, i = 0, -1
        bucket = capacity

        while i < len(plants)-1:

            if plants[i+1] <= bucket:

              bucket -= plants[i+1]
              i += 1
              steps += 1

            else:

              steps += 2*(i+1) + 1
              bucket = capacity - plants[i+1]
              i += 1
                
        return steps

        