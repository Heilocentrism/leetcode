# 73. Set Matrix Zeroes (Medium)
# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])
        first_row_zero = 0 in matrix[0]
        first_col_zero = any(row[0] == 0 for row in matrix)

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_col_zero:
            for row in matrix:
                row[0] = 0
        if first_row_zero:
            matrix[0] = [0] * cols