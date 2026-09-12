"""
LeetCode 200: Number of Islands
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

Approach: DFS or BFS to explore and mark visited land cells. 
Each time we find an unvisited land cell, we've found a new island.

Time Complexity: O(m * n) - we visit each cell at most once
Space Complexity: O(m * n) - worst case for recursion stack or queue
"""

def num_islands(grid):
    """
    Count the number of islands in a 2D grid.
    
    Args:
        grid: 2D list of characters representing the map ('1' = land, '0' = water)
        
    Returns:
        Number of islands
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    
    def dfs(r, c):
        """
        Depth-first search to mark all connected land as visited.
        """
        # Check boundaries and if cell is water or already visited
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            grid[r][c] == '0' or (r, c) in visited):
            return
        
        # Mark current cell as visited
        visited.add((r, c))
        
        # Explore all 4 directions (up, down, left, right)
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left
    
    islands = 0
    
    # Iterate through all cells
    for r in range(rows):
        for c in range(cols):
            # If we find unvisited land, we've found a new island
            if grid[r][c] == '1' and (r, c) not in visited:
                islands += 1
                dfs(r, c)  # Mark all connected land as visited
    
    return islands

# Test cases
if __name__ == "__main__":
    # Test case 1
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(f"Grid 1:")
    for row in grid1:
        print(row)
    print(f"Number of islands: {num_islands(grid1)}")  # Expected: 1
    print()
    
    # Test case 2
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(f"Grid 2:")
    for row in grid2:
        print(row)
    print(f"Number of islands: {num_islands(grid2)}")  # Expected: 3
    print()
    
    # Test case 3
    grid3 = [
        ["1","0","1","1","0","1","1"]
    ]
    print(f"Grid 3:")
    print(grid3)
    print(f"Number of islands: {num_islands(grid3)}")  # Expected: 3