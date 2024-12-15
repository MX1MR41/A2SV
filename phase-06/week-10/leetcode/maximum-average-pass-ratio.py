class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # heap
        # we utilize a greedy approach where for each extra student,
        # we add that student to the class whom adding one more student would cause
        # the biggest ratio change than adding that student to any other class
        # for each class, we calculate the change of ratio that would occur 
        # if we add one more student. Then we sort store them based on their respective
        # changes in a heap so we could get the class that has the highest change 
        # potential at any time

        heap = []

        for pas, tot in classes:
            curr_ratio = pas/tot # current ratio
            add_ratio = (pas + 1)/(tot + 1) # new ratio if we add one more student
            change = add_ratio - curr_ratio # the change that would occur
            
            # store with negative so we an get the maximum at any time
            heap.append((-change, pas, tot)) 
            
        heapify(heap)

        for _ in range(extraStudents):
            change, pas, tot = heappop(heap)
            pas += 1
            tot += 1
            change = (pas + 1)/(tot + 1) - pas/tot
            heappush(heap, (-change, pas, tot))

        return sum(i[1]/i[2] for i in heap)/len(heap)

        
