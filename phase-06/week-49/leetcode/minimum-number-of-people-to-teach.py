class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:


        for f in friendships:
            for i in range(len(f)):
                f[i] -= 1

        m = len(languages)

        cant = [set() for _ in range(m)]
        for i in range(len(friendships)):
            u, v = friendships[i]
            uknows = set(languages[u])
            vknows = set(languages[v])
            if not uknows.intersection(vknows):
                cant[u].add(v)
                cant[v].add(u)



        res = float("inf")
        for lang in range(1, n + 1):
            curr = 0
            temp_cant = [s.copy() for s in cant]
            temp_lang = [set(l) for l in languages]

            for i in range(m):
                for j in temp_cant[i]:
                    if lang not in temp_lang[i]:
                        curr += 1
                        temp_lang[i].add(lang)
                    if lang not in temp_lang[j]:
                        curr += 1
                        temp_lang[j].add(lang)


            res = min(res, curr)

        return res

