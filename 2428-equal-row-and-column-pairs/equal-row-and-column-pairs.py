class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        lines = {}
        count = 0
        
        for row in grid:
            lines[tuple(row)] = lines.get(tuple(row), 0) + 1
        
        for i in range(len(grid[0])):
            col = tuple(grid[j][i] for j in range(len(grid)))
            
            if col in lines:
                count += lines[col]
        
        return count
