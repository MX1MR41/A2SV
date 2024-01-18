class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.presum = []
        psum = 0
        for i in self.nums:
            psum += i
            self.presum.append(psum)
        

    def sumRange(self, left: int, right: int) -> int:
        if not right:
            if not left:
                return self.presum[right]

        if not left:
            return self.presum[right]

        return self.presum[right] - self.presum[left - 1]       