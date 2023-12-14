class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        HASH = defaultdict(int)

        for i in cpdomains:

            cnt, doms = i.split()
            dots = doms.count(".")
            HASH[doms] += int(cnt)
            
            for j in range(dots):
                doms = doms[doms.index(".") + 1:]
                HASH[doms] += int(cnt)

  

        return [f"{cnt} {dom}" for dom, cnt in HASH.items()]


        