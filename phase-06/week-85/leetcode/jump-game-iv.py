class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # bfs + grouping

        n = len(arr)

        group = defaultdict(set)

        for i in range(n):
            group[arr[i]].add(i)


        que = deque([(0, 0)])
        seen = set()
        seen_root = set()

        while que:
            for _ in range(len(que)):
                ind, steps = que.popleft()
                if ind == n - 1:
                    return steps

                root = arr[ind]
                if root not in seen_root:
                    inds = group[root]
                    inds.discard(ind)

                    for new_ind in inds:
                        if new_ind not in seen:
                            seen.add(new_ind)
                            que.append((new_ind, steps + 1))

                    seen_root.add(root)


                if ind + 1 < n and ind + 1 not in seen:
                    que.append((ind + 1, steps + 1))
                    seen.add(ind + 1)

                if ind - 1 >= 0 and ind - 1 not in seen:
                    que.append((ind - 1, steps + 1))
                    seen.add(ind - 1)



                
        
