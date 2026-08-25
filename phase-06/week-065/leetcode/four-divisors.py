class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def get_divs(x):
            divs = []

            for i in range(1, int(sqrt(x) + 1)):
                if x % i == 0:
                    j = x/i
                    divs.append(i)
                    if j != i:
                        divs.append(j)

                    if len(divs) > 4:
                        return 0


            return sum(divs) if len(divs) == 4 else 0


        return int(sum(get_divs(i) for i in nums))
                

        
