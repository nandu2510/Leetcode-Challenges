class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col = ord(coordinates[0]) - ord('a') + 1
        row = int(coordinates[1])
        
        if (col + row) % 2 == 1:
            return True
        else:
            return False 