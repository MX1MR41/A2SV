class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        folder.sort(key=lambda x: len(x))
        seen = set()

        for f in folder:
            n = len(f)
            temp = f.split("/")

            tempvar = ""
            flag = False
            for i in temp:
                if i:

                    tempvar += "/" + i

                    if tempvar in seen:
                        flag = True
                        break
            if not flag:
                seen.add(f)

        return list(seen)
