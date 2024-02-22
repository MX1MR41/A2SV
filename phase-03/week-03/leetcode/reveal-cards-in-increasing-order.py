class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n, queue = len(deck) - 1, deque()
        
        for _ in range(n):
            queue.appendleft(deck.pop()) 
            queue.appendleft(queue.pop())
        
        return deck + list(queue)
