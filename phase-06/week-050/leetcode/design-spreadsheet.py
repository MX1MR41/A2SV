class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0 for _ in range(26)] for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:

        col = ord(cell[:1]) - 65
        row = int(cell[1:]) - 1

        self.sheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:

        formula = formula[1:].split("+")
        X = formula[0]
        Y = formula[1]

        if X.isdigit():
            X = int(X)
        else:
            col = ord(X[:1]) - 65
            row = int(X[1:]) - 1
            X = self.sheet[row][col]

        if Y.isdigit():
            Y = int(Y)
        else:
            col = ord(Y[:1]) - 65
            row = int(Y[1:]) - 1
            Y = self.sheet[row][col]

        return X + Y
