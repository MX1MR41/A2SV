class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):

        self.food_ratings = {}

        self.food_to_cuisine = {}

        self.cuisine_heaps = defaultdict(list)

        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]

            self.food_ratings[food] = rating
            self.food_to_cuisine[food] = cuisine

            heappush(self.cuisine_heaps[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:

        self.food_ratings[food] = newRating

        cuisine = self.food_to_cuisine[food]

        heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:

        heap = self.cuisine_heaps[cuisine]

        while heap:

            current_rating_in_heap, food_name = heap[0]

            if -current_rating_in_heap == self.food_ratings[food_name]:

                return food_name
            else:

                heappop(heap)

        return ""
