class Solution:
    def validArrangement(self, pairs):
        # eulerian graph
        # represent the pairs as a node connected to another i.e [a,b] is (a) -> (b)
        # start node would have an outdegree greater than its indegree by one

        graph = defaultdict(list)
        inDegree, outDegree = defaultdict(int), defaultdict(int)

        # Build the adjacency list and track in-degrees and out-degrees
        for start, end in pairs:
            graph[start].append(end)
            outDegree[start] += 1
            inDegree[end] += 1

        result = []

        # Find the start node (outDegree == inDegree + 1)
        startNode = -1
        for node in outDegree:
            if outDegree[node] == inDegree[node] + 1:
                startNode = node
                break

        # If no such node exists, start from the first pair's first element
        if startNode == -1:
            startNode = pairs[0][0]

        nodeStack = [startNode]

        # Iterative DFS using stack
        while nodeStack:
            node = nodeStack[-1]
            if graph[node]:
                # Visit the next node
                nextNode = graph[node].pop(0)
                nodeStack.append(nextNode)
            else:
                # No more neighbors to visit, add node to result
                result.append(node)
                nodeStack.pop()

        # Reverse the result since we collected nodes in reverse order
        result.reverse()

        # Construct the result pairs
        pairedResult = []
        for i in range(1, len(result)):
            pairedResult.append([result[i - 1], result[i]])

        return pairedResult
