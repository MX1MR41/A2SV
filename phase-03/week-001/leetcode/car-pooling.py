class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        x = 0 # variable to store the max distance
        for trip in trips: # find the last dropoff location/max distance
            x = max(x,trip[-1])
            
        psum = [0 for _ in range(x + 1)] # and array to store the prefix sum
        
        # range update method by using prefix sum
        for passenger, start, end in trips: 
            psum[start] += passenger
            psum[end] -= passenger

        p = 0 # varable to store latest prefix sum
        for i in range(x + 1):
            p += psum[i]
            psum[i] = p

        for j in psum:
            if j > capacity: # if capacity is exceeded
                return False

        else:
            return True



