class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [ set() for r in range(9) ]
        cols = [ set() for c in range(9) ]
        boxes = [ set() for b in range(9) ]
        for row in range(9):
            for col in range(9):
                value=board[row][col]
                if value=='.':
                    continue
                box_idx=(row//3)*3 + (col//3)
                if ( value in rows[row] or value in cols[col] or value in boxes[box_idx]):
                    return False
                rows[row].add(value)
                cols[col].add(value)
                boxes[box_idx].add(value)
        return True

        