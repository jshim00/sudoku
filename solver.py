# A number is valid IFF it is not in the same row, not in the same column, and not in the same box 
def is_valid(bo, r, c, k):
    not_in_row = k not in bo[r]
    not_in_column = k not in [bo[i][c] for i in range(9)]
    not_in_box = k not in [bo[i][j] for i in range(r//3*3, r//3*3+3) for j in range(c//3*3, c//3*3+3)]
    return not_in_row and not_in_column and not_in_box

def solve(bo, r=0, c=0):
    if r == 9: # Termination 
        return True
    elif c == 9: # Move to beginning of next row and solve 
        return solve(bo, r+1, 0)
    elif bo[r][c] != 0: # If given, move to next space and solve
        return solve(bo, r, c+1)
    else: # If we are at an empty space: 
        for k in range(1, 10):
            if is_valid(bo, r, c, k):
                bo[r][c] = k
                if solve(bo, r, c+1): # Recursive condition: Work through until we have to backtrack 
                    return True
                bo[r][c] = 0 # backtracking: Revert to zero 
        return False
    
# bo = [
#     [0, 0, 4, 0, 5, 0, 0, 0, 0],
#     [9, 0, 0, 7, 3, 4, 6, 0, 0],
#     [0, 0, 3, 0, 2, 1, 0, 4, 9],
#     [0, 3, 5, 0, 9, 0, 4, 8, 0],
#     [0, 9, 0, 0, 0, 0, 0, 3, 0],
#     [0, 7, 6, 0, 1, 0, 9, 2, 0],
#     [3, 1, 0, 9, 7, 0, 2, 0, 0],
#     [0, 0, 9, 1, 8, 2, 0, 0, 3],
#     [0, 0, 0, 0, 6, 0, 1, 0, 0]
# ]

bo = [
    [0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 9, 4, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 5],
    [0, 9, 2, 3, 0, 5, 0, 7, 4],
    [8, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 6, 7, 0, 9, 8, 0, 0, 0],
    [0, 0, 0, 7, 0, 6, 0, 0, 0],
    [0, 0, 0, 9, 0, 0, 0, 2, 0],
    [4, 0, 8, 5, 0, 0, 3, 6, 0]
]

solve(bo)
print(*bo, sep='\n')