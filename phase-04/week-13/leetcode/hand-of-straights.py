class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # greedy + heap
        # start from the smallest number available then check if the other members are present
        # heap used to get the smallest element, hashmap used for quick membership check and count

        if len(hand) % groupSize: return False # mathematically impossible to divide accordingly

        cnt = Counter(hand)
        heapify(hand)
        
        while hand:
            # get rid of the numbers that have been exhausted
            while hand and not cnt[hand[0]]:
                heappop(hand)
            
            if hand: 
                num = heappop(hand)
            else: # exhausted the array
                break
            
            next_num = num + 1

            for _ in range(groupSize - 1):
                if cnt[next_num]:
                    cnt[next_num] -= 1
                    next_num += 1
                else:
                    return False
            
            cnt[num] -= 1
            if cnt[num]: # more of that number exist in the array
                heappush(hand, num)

        return True
