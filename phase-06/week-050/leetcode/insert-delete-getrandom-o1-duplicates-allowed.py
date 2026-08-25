# same as the original medium version of this problem except this time
# keep track of the indices that each number is located at using a set
# to remove an element, get the num at the end of the array, remove last_ind from the
# set of indices of the num found at the end of the array, and simply swap that num
# with any index of val to bring val to the end, then pop once from the array

class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.indices = defaultdict(set)

        

    def insert(self, val: int) -> bool:
        new = True
        if self.indices[val]:
            new = False

        self.arr.append(val)
        self.indices[val].add(len(self.arr) - 1)
        
        return new
        

    def remove(self, val: int) -> bool:
        if not self.arr or not self.indices[val]:
            return False

        if self.arr[-1] == val:
            last_ind = len(self.arr) - 1
            self.indices[val].discard(last_ind)
            self.arr.pop()
            return True

        last_num = self.arr[-1]
        last_ind = len(self.arr) - 1
        self.indices[last_num].discard(last_ind)

        val_ind = self.indices[val].pop()

        self.arr[val_ind], self.arr[last_ind] = self.arr[last_ind], self.arr[val_ind]
        self.arr.pop()

        self.indices[last_num].add(val_ind)

        
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
