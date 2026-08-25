class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        # bit manipulation +  greedy
        # let x be 111 in binary, which is 7
        # to make the a and a+1 as small as possible, we need to deconstruct as big of 
        # a chunk we cnan from x. And the bigest we can do here is to extract
        # 100 and 11 which are 4 and 3. We took the last MSB 1 from a
        # consecutive block of 1's starting from the LSB, and extracted it out,
        # so 111 becomes 100 and 11, 
        # and since all the bits behind it are 1, adding 1 to them will cause a carry chain
        # that will created that last MSB i.e. 11(3) + 1(1) = 100(4)
        
        def deconstruct(x):
            if x == 2:
                return -1

            pos = -1
            while x & (1 << (pos + 1)):
                pos += 1


            a = x & ~(1 << pos)

            return a

        print(deconstruct(int("1011", 2)))
 

        return [deconstruct(i) for i in nums]

            

            

            
