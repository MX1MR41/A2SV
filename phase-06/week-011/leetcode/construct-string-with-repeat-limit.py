class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # heap + stack
        # use a heap to instantly get the lexicographically largest letter
        # use a stack to build the string
        # store letters with their frequencies in both the heap and stack for ease
        
        cnt = Counter(s)
        heap = []
        for letter, freq in cnt.items():
            # store by decreasing order of lexicographical position
            heappush(heap, (-ord(letter), letter, freq))

        stack = []

        while heap:
            # just starting
            if not stack:
                o, letter, freq = heappop(heap)
                stack.append((letter, 1))
                # subtract 1 and if there are any remains, re-push into heap
                freq -= 1
                if freq:
                    heappush(heap, (o, letter, freq))

                continue

            
            last, c = stack[-1]
            
            if last == heap[0][1]:
                # get a smaller letter because repeatLimit has been reached
                if c >= repeatLimit:
                    temp = heappop(heap)
                    # if no more smaller letter
                    if not heap: 
                        break

                    o, letter, freq = heappop(heap)
    
                    freq -= 1
                    if freq:
                        heappush(heap, (o, letter, freq))

                    stack.append((letter, 1))
                    heappush(heap, temp)

                else:
                    o, letter, freq = heappop(heap)
                    freq -= 1
                    if freq:
                        heappush(heap, (o, letter, freq))
                    last, c = stack.pop()
                    c += 1
                    stack.append((last, c))

            else:
                o, letter, freq = heappop(heap)
                freq -= 1
                if freq:
                    heappush(heap, (o, letter, freq))

                stack.append((letter, 1))

        res = ""
        for letter, freq in stack:
            res += letter * freq

        return res



                    

                        
