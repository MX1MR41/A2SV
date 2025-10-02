class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
   

        
        for u, v in tickets:
            graph[u].append(v)

        for airport in graph:
            graph[airport].sort(reverse=True) # Sort descending to pop smallest
        
        itinerary = []
        
        def dfs(airport):
            

            while graph[airport]:
                next_destination = graph[airport].pop()
                dfs(next_destination)
            
            # if we have run out of flights from this airport, then this airport must be 
            # the next to last airport to be added to the itinerary
            itinerary.append(airport)

        
        dfs("JFK")
        
        
        return itinerary[::-1]
