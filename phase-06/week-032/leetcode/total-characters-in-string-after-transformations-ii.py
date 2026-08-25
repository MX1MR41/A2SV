"""
dp + matrix exponentiation
given an initial string, that can be modeled as a frequency vector, we are applying
similar operations over and over again on that vector so that the different frequencies
of the letters change with every transformation according to the given rules. For example, given 
the rules for transforming letters a to d like this [[2,1,1,0]], meaning a produces the next 2 letters, b produces the next 1, c the next 1 and d doesn't produce any. The rules can be represented as a matrix like this:

   a b c d
a [0,1,1,0]
b [0,0,1,0]
c [0,0,0,1]
d [0,0,0,0]

each row represent whether or not the row'th letter can produce the column'th letter. So a produces b and c because matrix[a][b] and matrix[a][c] are both 1.

given an inital string "abb", which can represented as [[1,2,0,0]] as a frequncy vector,
applying the given rules in the matrix to this vector can be simulated using matrix multiplication
we multiply the frequency vector by the transformation rules matrix

[[1,2,0,0]] x [[0,1,1,0],   which would give [[0,1,3,0]] i.e. the result would be "bccc"
               [0,0,1,0],
               [0,0,0,1],
               [0,0,0,0]]

this is one transformation. To perform another transformation, we multiply the result vector by the matrix one more time

[[0,1,3,0]] x [[0,1,1,0],   which would give [[0,0,1,3]] i.e. the result would be "cddd"
               [0,0,1,0],
               [0,0,0,1],
               [0,0,0,0]]

vector2 = vector1 x matrix = (vector0 x matrix) x matrix = vector0 x (matrix^2)

so to find the the t'th transformation, we multiply vector0 by matrix^t
to speed up the process of computing matrix^t, we can use matrix exponentiation, which is a similar technique to binary exponentiation, to compute the result in logt time
basically: x^n = x^(n/2) * x^(n/2), so we need to compute x^(n/2) only once, then multiply it by itself to find x^n.

"""

class Solution:
    def multiply(self, matA, matB):
        """
        Given two matrices matA and matB where num of cols of matA == num of rows in matB,
        this function performs matrix multiplication matA x matB and returns the result
        """

        rows = len(matA)
        cols = len(matB[0])

        res = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            row = matA[r]
            for c in range(cols):
                col = [matB[i][c] for i in range(cols)]

                cell = 0
                for i in range(cols):
                    cell = (cell + row[i] * col[i]) % self.MOD

                res[r][c] = cell

        return res

    def power(self, mat, exponent):
        """
        Given a matrix mat and an integer exponent, this function computes the result of raising
        mat to the power of exponent. It does this in a binary exponentiation method
        """

        if exponent == 1:
            return mat

        half = self.power(mat, exponent // 2)

        res = self.multiply(half, half)

        if exponent % 2 == 1:
            res = self.multiply(mat, res)

        return res

    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:

        self.MOD = 10**9 + 7
        N = 26

        # the matrix that will represent the transformation rules where
        # transform_matrix[i][j] = 1 if the i'th letter can produce the jth letter, else 0
        transform_matrix = [[0 for _ in range(N)] for _ in range(N)]

        # populate the transform_matrix
        for i in range(len(nums)):
            steps = nums[i]

            for step in range(1, steps + 1):
                nxt = (i + step) % N
                transform_matrix[i][nxt] = 1

        
        # raise the transform_matrix to the power of t, where t is the number of transformations
        powered_matrix = self.power(transform_matrix, t)


        # a single row matrix (or vector) that will store the freqs of each letter intially
        freqs = [[0 for _ in range(N)]]

        for letter in s:
            freqs[0][ord(letter) - 97] += 1


        # multiply the frequency vector by the powered_matrix to simulate the transformations
        res = self.multiply(freqs, powered_matrix)

        # count length and return
        tot = 0
        for i in res[0]:
            tot = (tot + i) % self.MOD

        return tot
