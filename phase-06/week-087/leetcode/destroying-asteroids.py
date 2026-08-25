class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for a in asteroids:
            if mass >= a:
                mass += a
            else:
                return False

        return True
        
