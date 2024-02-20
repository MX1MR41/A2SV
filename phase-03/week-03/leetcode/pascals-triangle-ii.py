class Solution:
    def getRow(self, rowIndex: int):
        if rowIndex == 0:
            return [1]
        else:
            prev_row = self.getRow(rowIndex - 1)
            curr_row = [1] + [prev_row[i - 1] + prev_row[i] for i in range(1, rowIndex)] + [1]
            return curr_row
