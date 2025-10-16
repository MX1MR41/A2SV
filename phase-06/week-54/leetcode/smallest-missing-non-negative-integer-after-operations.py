class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # MEX
        # to form a number x by subtracting/adding value from/to a num from nums,
        # the num - x should be divisible by zero, that is because we can keep doing
        # the operation by value until we reach x from n
        # i.e. (num - x) % value = 0; 
        #      (num % value) - (x % value) = 0
        #      (num % value) = (x % value)
        # therefore, x can be formed it there exists a num in nums whose modulo 
        # is equal to the modulo of x
        
        arr = [num % value for num in nums]

        count = Counter(arr)
        mex = 0

        while True:
            mod = mex % value
            if count[mod] > 0:
                count[mod] -= 1
                mex += 1
            else:
                return mex
