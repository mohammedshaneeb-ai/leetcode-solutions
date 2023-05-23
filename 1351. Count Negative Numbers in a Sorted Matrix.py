def countNegative(grid):
    count = 0 # Initializing count as Zero
    for i in range(len(grid)): # Traversing through Rows
        for j in range(len(grid[i])):# Traversing through Columns
            # if value less than zero we increase the count
            if grid[i][j] < 0:
                count +=1
    return count # Returning the count

# Example 1
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Expected Output : 8


# Example 2
grid = [[3,2],[1,0]]
# Expected Output : 0

# Calling function
print(countNegative(grid))

