class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        heap = [-int(i) for i in num]
        heapify(heap)

        for i in range(len(num)):
            if int(num[i]) != -heap[0]:
                r = len(num) - 1
                print(r, len(num))
                while int(num[r]) != -heap[0]:
                    r -= 1

                num[i], num[r] = num[r], num[i]
                break

            heappop(heap)

        # print(num)

        return int("".join(num))
        
