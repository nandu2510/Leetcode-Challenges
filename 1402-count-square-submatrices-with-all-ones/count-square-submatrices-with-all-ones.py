class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        total = 0

        # We can modify the input matrix directly as DP table
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i > 0 and j > 0:
                        matrix[i][j] = min(
                            matrix[i-1][j], 
                            matrix[i][j-1], 
                            matrix[i-1][j-1]
                        ) + 1
                    total += matrix[i][j]
        return total
