class Solution(object):
    def findDuplicate(self, paths):
        files = collections.defaultdict(list)
        for p in paths:
            temp = p.split(" ")
            for i in range(1, len(temp)):
                fname = temp[0] + "/" + temp[i][0:temp[i].find("(")]
                file_content = temp[i][temp[i].find("(") + 1:temp[i].find(")")]
                files[file_content].append(fname)
        res = []
        for file_content, file_names in files.items():
            if len(file_names) > 1:
                res.append(file_names)
        return res
