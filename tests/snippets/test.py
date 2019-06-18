def spiralOrder(matrix):
    visited = set()
    arr = []
    d = 0
    
    #get number of cells
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    cells = num_rows * num_cols
    
    cells_visited = 0
    row = 0
    col = 0
    prev_row = 0
    prev_col = 0
    """
    1. keep track of visited cells
    2. keep track of directions
        - Traverse right until the edge or a visited cell
        - Traverse down until edge or visited cell
        - Traverse left until edge or visited cell
        - Traverse up until edge or visited cell
    """ 
    while( cells_visited <= cells ):
        hit_right = col >= num_cols
        hit_bottom = row >= num_rows
        hit_left = col < 0
        hit_top = row < 0
        
        num = matrix[row][col]

        if num in visited or hit_right or hit_bottom or hit_left or hit_top:
            d += 1
            if d == 4:
                d = 0
            if num in visited:
                print(f"row: {row}  col: {col}")
                row = prev_row
                col = prev_col
        else:
            visited.add(num)
            arr.append(num)
            # print(num)

        prev_row = row
        prev_col = col
            
        if d == 0: # go right
            if (col < num_cols - 1):
                col += 1
        elif d == 1: # go down
            if row < num_rows - 1:
                row +=1 
        elif d == 2: # go left
            if col > 0:
                col -= 1
        elif d == 3: # go up
            if row > 0:
                row -= 1
        
        cells_visited += 1


input = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

spiralOrder(input)