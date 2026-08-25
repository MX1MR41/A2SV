class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        # backtracking  + dp memoization
        # simulate the process per match per round, branching out to two choices if the players
        # are NPCs else choose the main players
        # memoize the configurations of the firstPlayer and secondPlayer in arrays of different
        # lengths, so that if you see _ _ _ 1stP _ _ 2ndP _ _ a second time, you won't go down
        # that path cuz you have previously explored such a path and computed what the 
        # earliest and latest round could be

        earliest = float("inf")
        latest = 0


        seen = set()
    
        def dfs(arr, match, round, winners):
            nonlocal earliest, latest
            
            n = len(arr)

            # the positions of the current playing player, 
            # match-distance from both ends of the array
            l, r = match, n - 1 - match

            # run out of match-ups for this round
            if l > r:
                # set up for new round
                arr = sorted(winners)

                winners = []
                round += 1
                match = 0

                first_ind = arr.index(firstPlayer)
                second_ind = arr.index(secondPlayer)

                # such configuration has been seen before, no need to recompute
                if (first_ind, second_ind, len(arr)) in seen:
                    return

                # memoize
                seen.add((first_ind, second_ind, len(arr))) 

            # single player edge case
            if l == r:
                arr = sorted(winners + [arr[l]])

                winners = []
                round += 1
                match = 0

                first_ind = arr.index(firstPlayer)
                second_ind = arr.index(secondPlayer)

                if (first_ind, second_ind, len(arr)) in seen:
                    return

                seen.add((first_ind, second_ind, len(arr)))
            

            n = len(arr)
            l, r = match, n - 1 - match
            
            # main players finally meet
            if sorted([arr[l], arr[r]]) == sorted([firstPlayer, secondPlayer]):
                earliest = min(earliest, round)
                latest = max(latest, round)
                return

            # main players defeating NPC players
            if arr[l] in [firstPlayer, secondPlayer]:
                dfs(arr, match + 1, round, winners + [arr[l]])
                return
            
            if arr[r] in [firstPlayer, secondPlayer]:
                dfs(arr, match + 1, round, winners + [arr[r]])
                return


            # try either of the NPC players defeating the other
            dfs(arr, match + 1, round, winners + [arr[l]])
            dfs(arr, match + 1, round, winners + [arr[r]])



        
        dfs([i for i in range(1, n + 1)], 0, 1, [])
        
        return [earliest, latest]

