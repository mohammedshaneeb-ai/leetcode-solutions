def countNegative(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] < 0:
                count +=1
    
    return count

# Example 1
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Expected Output : 8


# Example 2
grid = [[3,2],[1,0]]
# Expected Output : 0


print(countNegative(grid))

