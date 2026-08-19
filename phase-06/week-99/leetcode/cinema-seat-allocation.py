class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        #  binary search
        reservedSeats.sort()

        def isFree(row, seat):
            l, r = 0, len(reservedSeats) - 1
            start = r + 1
            while l <= r:
                mid = (l + r) // 2
                if reservedSeats[mid][0] >= row:
                    start = mid
                    r = mid - 1
                else:
                    l = mid + 1

            ind = start
            while ind < len(reservedSeats) and reservedSeats[ind][0] == row:
                if reservedSeats[ind][1] == seat:
                    return False

                ind += 1

            return True

        def checkRow(row):
            block1 = (
                isFree(row, 2) and isFree(row, 3) and isFree(row, 4) and isFree(row, 5)
            )
            block2 = (
                isFree(row, 6) and isFree(row, 7) and isFree(row, 8) and isFree(row, 9)
            )

            block3 = (
                isFree(row, 4) and isFree(row, 5) and isFree(row, 6) and isFree(row, 7)
            )

            if block1 and block2:
                return 2

            if block1 or block2 or block3:
                return 1

            return 0

        rows = set([i[0] for i in reservedSeats])

        res = 2 * n

        for row in rows:
            res -= 2

            count = checkRow(row)

            res += count

        return res
