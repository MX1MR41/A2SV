# heap
# requirements:
# 1) cheapest 5 shops per movie => heap per movie
# 2) cheapest 5 rented movies => global heap for rented movies
# 3) renting and returning a movie from s epecific shop => set per shop
# kKep track of the movies that each shop has along with their prices in a dict
# dict[shop][movie] = price, do this for both rental and ownership of movies
# Keep track of the cheapest movies rented globally using a heap,
# and use a set to keep track of rented movies in a (price, shop, movie) manner
# Keep track of the cheapest shops per movie using a dictionary and heaps
# dict[movie] = heap of (price, shop) tuples

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.shop_has = defaultdict(dict) # shop_has[shop][movie] = price
        self.shop_rented = defaultdict(dict) # shop_rented[shop][movie] = prices

        self.rented = [] # heap
        self.rented_set = set()


        self.movie = defaultdict(list) # movie[movie] = heap
        self.movie_set = set()


        for shop, movie, price in entries:
            self.shop_has[shop][movie] = price

            self.movie_set.add((price, shop, movie))

            heappush(self.movie[movie], (price, shop))


    def search(self, movie: int) -> List[int]:
        res = []

        while len(res) < 5 and self.movie[movie]:
            price, shop = heappop(self.movie[movie])

            # either the movie has been rented out or it didn't exist
            if (price, shop, movie) not in self.movie_set:
                continue

            # remove it from the set so that if there is a duplicate in the heap, 
            # it will not be considered
            self.movie_set.discard((price, shop, movie))

            res.append((price, shop))

        # re-adding onto the heap and set
        for price, shop in res:
            heappush(self.movie[movie], (price, shop))
            self.movie_set.add((price, shop, movie))

        res.sort()
        return [shop for price, shop in res] if res else []
        

    def rent(self, shop: int, movie: int) -> None:
        
        # get price
        price = self.shop_has[shop][movie]
        del self.shop_has[shop][movie]

        # rent out
        self.shop_rented[shop][movie] = price

        # add to heap and set of rental
        heappush(self.rented, (price, shop, movie))
        self.rented_set.add((price, shop, movie))
        
        # discard from global ownership set
        self.movie_set.discard((price, shop, movie))
        

    def drop(self, shop: int, movie: int) -> None:
        # get price
        price = self.shop_rented[shop][movie]
        del self.shop_rented[shop][movie]
        
        # return movie
        self.shop_has[shop][movie] = price

        # re-add onto the heap and global ownership set
        heappush(self.movie[movie], (price, shop))
        self.movie_set.add((price, shop, movie))

        # remove from the global rental set
        self.rented_set.discard((price, shop, movie))
        

    def report(self) -> List[List[int]]:
        res = []
        while len(res) < 5 and self.rented:
            price, shop, movie = heappop(self.rented)

            # either the movie hasn't been rented out or it didn't exist
            if (price, shop, movie) not in self.rented_set:
                continue

            # remove it from the set so that if there is a duplicate in the heap, 
            # it will not be considered
            self.rented_set.discard((price, shop, movie))

            res.append((price, shop, movie))

        # re-adding onto the heap and set
        for item in res:
            heappush(self.rented, item)
            self.rented_set.add(item)
            

        res.sort()

        return [[shop, movie] for price, shop, movie in res] if res else []
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
