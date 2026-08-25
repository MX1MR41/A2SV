class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1 or not encodedText.strip():
            return encodedText

        cols = len(encodedText) // rows
        mat = [["" for _ in range(cols)] for _ in range(rows)]

        i = j = 0
        t = 0
        while t < len(encodedText):
            mat[i][j] = encodedText[t]
            j += 1
            if j == cols:
                i += 1
                j = 0

            t += 1

        i = j = last_j = 0

        res = ""
        count = 0
        while True:

            res += mat[i][j]
            i += 1
            j += 1
            if i == rows:
                i = 0
                j = last_j + 1
                last_j = j

            if j == cols:
                break

        return res.rstrip()
