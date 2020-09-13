board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


# The algorithm that will use these functions and backtrack for us
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10): #Loop through the values from 1-9
        if valid(bo, i, (row, col)): # Check if by adding that number to our board it would be a valid solution
            bo[row][col] = i # If it's valid we add it into the board

            if solve(bo): # Recursively try to finish the solution by calling solve() on our new board
                return True
            bo[row][col] = 0

    return False # If we loop through tht numbers and none of them are valid, we return false

# Find if the current board is valid
def valid(bo, num, pos):

    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
                  return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True



# Print the board out
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ") #Print a horizontal line when on a third row

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8: #Check if in the last position
                print(bo[i][j]) #Do that backslash and go to the next line
            else:
                print(str(bo[i][j]) + " ", end="") #end means stay on the same line when we keep printing things

# Find empty spaces
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row, col  # which is a tuple

    return None

# print_board(board)
# solve(board)
# print("_________________________")
# print_board(board)