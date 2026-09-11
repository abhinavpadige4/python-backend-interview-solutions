# Solution for LeetCode 36: Valid Sudoku
class Solution:
    def isValidSudoku(self, board):
        """
        Determine if a 9x9 Sudoku board is valid.
        
        Time Complexity: O(1) - we always check 81 cells (9x9)
        Space Complexity: O(1) - we use fixed size sets (at most 9*3 = 27 elements)
        
        Args:
            board: 9x9 2D list representing the Sudoku board
            
        Returns:
            True if the Sudoku board is valid, False otherwise
        """
        # Initialize sets to track seen numbers in rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                
                # Check row
                if num in rows[i]:
                    return False
                rows[i].add(num)
                
                # Check column
                if num in cols[j]:
                    return False
                cols[j].add(num)
                
                # Check 3x3 box
                box_index = (i // 3) * 3 + (j // 3)
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)
        
        return True

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Valid Sudoku
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print("Test 1 (Valid):", solution.isValidSudoku(board1))  # Expected: True
    
    # Test case 2: Invalid Sudoku (duplicate in first row)
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print("Test 2 (Invalid):", solution.isValidSudoku(board2))  # Expected: False