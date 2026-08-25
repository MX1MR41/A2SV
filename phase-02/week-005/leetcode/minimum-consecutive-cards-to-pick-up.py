class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        min_pickup = float("inf")
        card_count = defaultdict(int)
        
        for right in range(len(cards)):
            card = cards[right]
            card_count[card] += 1

            
            while card_count[card] > 1:
                min_pickup = min(min_pickup, right - left + 1)
                card_count[cards[left]] -= 1
                left += 1
        
        return min_pickup if min_pickup != float("inf") else -1
