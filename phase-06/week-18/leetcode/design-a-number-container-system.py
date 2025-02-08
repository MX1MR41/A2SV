class NumberContainers:

    def __init__(self):
        self.num_at_ind = defaultdict(int)
        self.inds_of_num = defaultdict(list)

        

    def change(self, index: int, number: int) -> None:
        num = self.num_at_ind[index]
        
        self.num_at_ind[index] = number
        heappush(self.inds_of_num[number], index)
        

        

    def find(self, number: int) -> int:
        if number not in self.inds_of_num:
            return - 1

        heap = self.inds_of_num[number]
        while heap and self.num_at_ind[heap[0]] != number:
            heappop(heap)

        if not heap:
            return -1

        return heap[0]
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
