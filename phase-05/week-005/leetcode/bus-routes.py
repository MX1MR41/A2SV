class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # instead of graphing bus to bus, we graph stop to stop if they have common buses
        # then bfs for finding least number of buses it takes to travel 
        # from the stop(s) where the source bus is located to any stop(s) that has the target

        if source == target: 
            return 0

        g = defaultdict(set)
        stops = defaultdict(set) # {bus: set(stops that have that bus)}

        for stop, buses in enumerate(routes):
            for b in buses:
                stops[b].add(stop)

        if stops[source].intersection(stops[target]):
            return 1

        # construct graph from stop to stop
        for bus, stps in stops.items():
            if len(stps) > 1: # this bus is in multiple stops so connect every stop that has it
                stps = list(stps)
                for i in range(len(stps)):
                    for j in range(i + 1, len(stps)):
                        g[stps[i]].add(stps[j])
                        g[stps[j]].add(stps[i])

        ans = 1
        que = deque(list(stops[source]))
        visited = set()

        while que:
            for _ in range(len(que)):
                curr = que.popleft()
                if curr in stops[target]:
                    return ans

                if curr in visited:
                    continue

                visited.add(curr)
                que.extend(list(g[curr]))

            ans += 1

        return -1
