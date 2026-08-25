class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # dp with four variables that count the types of numbers to the left and right
        # then multiplying to find all possibilities

        n = len(rating)
        ans = 0
        for i in range(1, n-1):
            left_lesser = left_greater = right_greater = right_lesser = 0
            num = rating[i]
            for j in range(n):
                num_2 = rating[j]
                if num_2 < num:
                    if j < i:
                        left_lesser += 1
                    else:
                        right_lesser += 1
                elif num_2 > num:
                    if j < i:
                        left_greater += 1
                    else:
                        right_greater += 1
                        
            ans += left_lesser * right_greater
            ans += left_greater * right_lesser
            
       
        return ans
