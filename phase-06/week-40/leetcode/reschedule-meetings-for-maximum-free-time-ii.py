class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        # greedy + prefix sum (prefix max)
        # given ...[gap1][meeting1][gap2]..., if we move meeting1 to some time outside this
        # range, the new gap we will have will be gap1 + meeting1_length + gap2.
        # But we can only move meeting1 to some time outside this range iff there exists a
        # gap that could accomodate it... i.e. there must be some gap before gap1 or after
        # gap2 whose size is >= meeting_length. To find out if such a gap exists, we can 
        # precompute and store the prefix and suffix maximum gap seen so far for each index.
        # If no such gap exists, we can just reconfigure it to be [gap1][gap2][meeting1]
        # so the new gap will be gap1 + gap2



        n = len(startTime)

        timeline = [startTime[0]]

        for i in range(n - 1):
            timeline.append([startTime[i], endTime[i]])
            timeline.append(startTime[i + 1] - endTime[i])

        timeline.append([startTime[-1], endTime[-1]])
        timeline.append(eventTime - endTime[-1])

        pre_max = []
        m = len(timeline)
        pre = 0
        for i in range(0, m, 2):
            pre_max.append(pre)
            pre_max.append(pre)
            pre = max(pre, timeline[i])

        pre_max.pop()

        suf_max = []
        suf = 0
        for i in range(m - 1, -1, -2):
            suf_max.append(suf)
            suf_max.append(suf)
            suf = max(suf, timeline[i])
        
        suf_max.pop()
        suf_max.reverse()

   
        res = 0

        for i in range(0, m - 1, 2):
            left_gap = timeline[i]
            right_gap = timeline[i + 2]
            meeting_len = timeline[i + 1][1] - timeline[i + 1][0]

            pre = pre_max[i]
            suf = suf_max[i + 2]

            if pre >= meeting_len or suf >= meeting_len:
                res = max(res, left_gap + meeting_len + right_gap)
            else:
                res = max(res, left_gap + right_gap)

        return res

