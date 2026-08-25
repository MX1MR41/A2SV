class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bfs
        # instead of mapping each word to the other by counting their difference,
        # map each word to all the matching pattersn i.e hot -> *ot, h*t, ho*.
        # then for every word in bfs que, try all possible patterns for that word.
        # ex: graph = {ho* : [hot], h*t : [hot], *ot : [hot]}
        
        if endWord not in wordList:
            return 0

        graph = defaultdict(list)
        word_len = len(beginWord)

        for word in wordList:
            for i in range(word_len):
                pattern = word[:i] + "*" + word[i + 1 :]
                graph[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:

            current_word, level = queue.popleft()

            for i in range(word_len):
                pattern = current_word[:i] + "*" + current_word[i + 1 :]

                for nei in graph[pattern]:
                    if nei == endWord:
                        return level + 1
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, level + 1))

        return 0
