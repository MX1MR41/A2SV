class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # count the length of the longest common prefix between the two sentences
        # and the longest suffix too. If the summation of these two is greater than or equal to
        # the length of the shorter sentence, then it is possible to add an arbitrary (only one) sentence
        # either in the middle, beginning or end of the shorter sentence

        s1 = sentence1.split()
        s2 = sentence2.split()

        if len(s1) <= len(s2):
            sen1, sen2 = s1, s2
        else:
            sen1, sen2 = s2, s1

        l1 = l2 = 0
        r1, r2 = len(sen1) - 1, len(sen2) - 1
        count = 0

        pre = 0
        while l1 < len(sen1) and l2 < len(sen2) and sen1[l1] == sen2[l2]:
            pre += 1
            l1 += 1
            l2 += 1

        suff = 0
        while r1 >= 0 and r2 >= 0 and sen1[r1] == sen2[r2]:
            suff += 1
            r1 -= 1
            r2 -= 1

        return len(sen1) - pre - suff <= 0
