class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # simulation
        # to find the letter at index k without generating the whole string,
        # retrace the steps or previous indices that generated index k
        # then simulate the operations one by one

        steps = [] # the prev indices that generated k
        curr = k

        while curr > 1:
            steps.append(curr)

            size = 2 ** ceil(log2(curr)) # the size of the string when curr was generated
            mid = size // 2

            # we find the mirror index from the left half that generated curr
            dist_from_mid = curr - mid
            prev = dist_from_mid

            # move one step backwards
            curr = prev
        


        letter = 0
        size = 1

        for i in range(len(operations)):

            size *= 2
            mid = size // 2


            # if we have generated a string of size big enough to contain the next index
            if steps and steps[-1] <= size:
                step = steps.pop()

                # if it is in the second half, increment by 1 if operations[i] == 1
                if step > mid and operations[i] == 1:
                    letter = (letter + 1) % 26

            if not steps:
                break


        return chr(letter + 97)
