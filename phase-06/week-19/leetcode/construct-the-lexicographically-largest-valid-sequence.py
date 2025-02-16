class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # backtracking
        # instead of tying to fill the numbers in descending order at available spots.
        # fill every current empty index with the largest number that would give
        # a proper sequence


        m = 1 + 2*(n - 1) # size of the result array

        def dfs(ind, arr, used):
            
            # move the index forward till you find an empty spot
            while ind < m and arr[ind]:
                ind += 1

            # run out of empty spots
            if ind >= m:
                # if every spot has been filled out, return the array
                # else if there exists even one empty spot, return a flushed array
                return arr if 0 not in arr else [0]*m

            res = arr

            # start from the largest possible number that hasn't been used yet
            for num in range(n, 0, -1):
                if num not in used:

                    # add 1 to only one spot
                    if num == 1:
                        temp = arr[:]
                        temp[ind] = num
                        used.add(num)
                        cand = dfs(ind + 1, temp, used)
                        # if a valid candidate is found, break immediately
                        if 0 not in cand:
                            res = cand
                            break

                        # else undo what you did and try the next available options
                        used.discard(num)
                        
                    # add the non-1 number at two spots  
                    else: 
                        if ind + num < m and not arr[ind + num]:
                            temp = arr[:]
                            temp[ind] = temp[ind + num] = num
                            used.add(num)
                            
                            cand = dfs(ind + 1, temp, used)
                            if 0 not in cand:
                                res = cand
                                break

                            used.discard(num)

    
            return res


        return dfs(0, [0]*m, set())

