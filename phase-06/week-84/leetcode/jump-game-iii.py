class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        #  graph it, bfs i

        n = len(arr)

        g = defaultdict(list)


        zeros = set()
        for i in range(n):
            if arr[i] == 0:
                zeros.add(i)

        if start in zeros:
            return True
        
        if not zeros:
            return False

        n = len(arr)
        for i in range(n):
            num = arr[i]

            h = i - num
            if h >= 0:
                g[i].append(h)


            j = i + num
            if j < n:
                g[i].append(j)

        seen = set()
        que = deque([start])

        while que:
            for _ in range(len(que)):
                i = que.popleft()
                if i in seen:
                    continue

                seen.add(i)

                if i in zeros:
                    return True


                for j in g[i]:
                    if j not in seen:
                        que.append(j)

        return False



                

        
