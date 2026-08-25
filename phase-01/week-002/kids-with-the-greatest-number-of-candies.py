class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest = max(candies)
        result = []

        for i in candies:
            result.append(i + extraCandies >= largest)

        return result
        