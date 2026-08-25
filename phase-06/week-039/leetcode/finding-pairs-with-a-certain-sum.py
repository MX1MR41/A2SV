class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2_map = {ind: num for ind, num in enumerate(nums2)}
        self.freq = Counter(nums2)
        

    def add(self, index: int, val: int) -> None:
        num_at_index = self.nums2_map[index]
        new_num = num_at_index + val

        self.freq[num_at_index] -= 1

        self.nums2_map[index] = new_num

        self.freq[new_num] += 1
        

    def count(self, tot: int) -> int:
        total = 0
        for num in self.nums1:
            complement = tot - num
            total += self.freq[complement]

        return total
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
