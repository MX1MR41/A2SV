class RandomizedSet:

    def __init__(self):
        
        self.HASH = {}
        self.nums = []

    def insert(self, val: int) -> bool:

        if val not in self.HASH:
            self.HASH[val] = len(self.nums)
            self.nums.append(val)
            return True

        return False

    def remove(self, val: int) -> bool:

        if val in self.HASH:
            self.HASH[self.nums[-1]] = self.HASH[val]
            self.nums[self.HASH[val]] = self.nums[-1]
            self.nums.pop()
            self.HASH.pop(val)
            return True

        return False

    def getRandom(self) -> int:
        
        return random.choice(self.nums)
