import math

def encryption(s):
    # Remove spaces from the input string
    s = s.replace(" ", "")
    # Calculate the number of rows and columns
    l = len(s)
    rows = math.floor(math.sqrt(l))
    cols = math.ceil(math.sqrt(l))
    # If the grid is too small, adjust rows
    if rows * cols < l:
        rows += 1
    # Create the grid
    grid = []
    for i in range(rows):
        row = s[i*colums : (i+1)*colums]
        grid.append(row)
    # Encrypt the string
    encrypted = ""
    for j in range(colums):
        for i in range(rows):
            if j < len(grid[i]):
                encrypted += grid[i][j]
        encrypted += " "
    return encrypted.strip()

# Read the input string
s = input().strip()
# Encrypt the input string
result = encryption(s)
print(result)
