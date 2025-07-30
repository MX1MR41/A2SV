class Solution:
    def reorganizeString(self, s: str) -> str:
        # greedy + heap
        # prioritize the letters with the highest frequencies to be the next letter
        # so that we can distribute them more. For that, heap can be used where the top
        # element is the letter with the highest frequency

        n = len(s)

        count = Counter(s)

        heap = []

        for letter, cnt in count.items():
            heappush(heap, (-cnt, letter))

        res = ""
        while heap:
            if not res:
                negcnt, letter = heappop(heap)
                res += letter
                negcnt += 1
                if negcnt != 0:
                    heappush(heap, (negcnt, letter))

                continue

            if heap[0][1] != res[-1]:
                negcnt, letter = heappop(heap)
                res += letter
                negcnt += 1
                if negcnt != 0:
                    heappush(heap, (negcnt, letter))
            else:
                if len(heap) < 2:
                    return ""

                first = heappop(heap)
                negcnt, letter = heappop(heap)
                res += letter
                negcnt += 1
                if negcnt != 0:
                    heappush(heap, (negcnt, letter))

                heappush(heap, first)

        return res
