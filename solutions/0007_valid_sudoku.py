"""
LeetCode 36: Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated 
according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Approach: Use hash sets to track seen numbers in rows, columns, and 3x3 boxes.

Time Complexity: O(1) - board size is fixed at 9x9
Space Complexity: O(1) - we use fixed-size data structures
"""

def is_valid_sudoku(board):
    """
    Determine if a Sudoku board is valid.
    
    Args:
        board: 9x9 list of lists representing the Sudoku board
               Empty cells are represented by '.'
        
    Returns:
        True if the board is valid, False otherwise
    """
    # Initialize sets for rows, columns, and boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            cell = board[i][j]
            if cell == '.':
                continue
                
            # Check if cell value is valid
            if not cell.isdigit() or int(cell) < 1 or int(cell) > 9:
                return False
            
            num = int(cell)
            box_index = (i // 3) * 3 + j // 3
            
            # Check if number already exists in row, column, or box
            if (num in rows[i] or 
                num in cols[j] or 
                num in boxes[box_index]):
                return False
            
            # Add number to the respective sets
            rows[i].add(num)
            cols[j].add(num)
            boxes[box_index].add(num)
    
    return True

# Test cases
if __name__ == "__main__":
    # Valid Sudoku board
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
    print(f"Board 1 is valid: {is_valid_sudoku(board1)}")  # Expected: True
    print()
    
    # Invalid Sudoku board (duplicate in first row)
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
    print(f"Board 2 is valid: {is_valid_sudoku(board2)}")  # Expected: False