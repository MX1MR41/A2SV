class Solution(object):
    def carPooling(self, trips, capacity):
        pos = [x for num, start, end in trips for x in [[start, num], [end, -num]]]
        pos.sort()
        for _, new in pos:
            capacity -= new
            if capacity < 0:
                return False
        return True