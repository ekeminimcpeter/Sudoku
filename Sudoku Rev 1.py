# Author: Ekemini Peter
# Date: 01/01/2025
# Revision: 1
# Description: Original implementation of sudoku
# Scope:
#   Reads 9 rows of the Sudoku, each containing 9 digits
#   check carefully if the data entered are valid
#   Outputs Yes if the Sudoku is valid, and No otherwise
#################################################################################


# Collect user input for board rows and check for data validity
input_rows = [] #list to hold input for board's rows

try:
    for row in range(1,10):
        print("Enter digits for board's row",row,"below")
        input_row = input()
        if input_row.isdigit():
            input_rows.append(input_row)

        else:
            raise ValueError
        
    # Construct rows for board's matrix
    board_rows = [] #list to hold rows values extracted (integer) from input rows (string) 

    for i in range(9):
        board_rows.append([int(input_row) for input_row in input_rows[i]]) # Nested list generator expression

    # Construct columns for board's matrix: transpose of matrix rows
    board_columns = [] #list to hold columns values extracted (integer) from input columns (string)

    for i in range(9):
        board_columns.append([int(input_row[i]) for input_row in input_rows]) 

    # Construct 3x3 sub-square for board's matrix
    boards_sub_squares = [ board_rows[0][0:3] + board_rows[1][0:3] + board_rows[2][0:3], #sub-sqaure 1
                           board_rows[0][3:6] + board_rows[1][3:6] + board_rows[2][3:6], #sub-sqaure 2
                           board_rows[0][6:] + board_rows[1][6:] + board_rows[2][6:], #sub-sqaure 3
                           board_rows[3][0:3] + board_rows[4][0:3] + board_rows[5][0:3], #sub-sqaure 4
                           board_rows[3][3:6] + board_rows[4][3:6] + board_rows[5][3:6], #sub-sqaure 5
                           board_rows[3][6:] + board_rows[4][6:] + board_rows[5][6:], #sub-sqaure 6
                           board_rows[6][0:3] + board_rows[7][0:3] + board_rows[8][0:3], #sub-sqaure 7
                           board_rows[6][3:6] + board_rows[7][3:6] + board_rows[8][3:6], #sub-sqaure 8
                           board_rows[6][6:] + board_rows[7][6:] + board_rows[8][6:], #sub-sqaure 9
                            ]

    # Construct sum of rows, sum of colums sub_squares
    list_sum_of_row_digits = [] #list containing the sum of digits of each board's row
    for row in board_rows:
        list_sum_of_row_digits.append(sum(row))

    list_sum_of_column_digits =[] #list containing the sum of digits of each board's column
    for column in board_columns:
        list_sum_of_column_digits.append(sum(column))

    list_sum_of_sub_square_digits = [] #list containing the sum of digits of each board's sub_square
    for sub_square in boards_sub_squares:
        list_sum_of_sub_square_digits.append(sum(sub_square))
                
    # Compare sum of rows, columns and sub-squares for validity for sudoku 
    valid_list = [45]*9 #ideal list for sum of sudoku rows, columns and sub_sqaures

    if list_sum_of_row_digits == valid_list and list_sum_of_column_digits == valid_list and list_sum_of_sub_square_digits == valid_list:
        print("\n\n -------------------------\n|   Yes, it's a sudoku!    |\n -------------------------") #output result
    else:
        print("\n\n -------------------------\n| Oops, it's not a sudoku! |\n -------------------------") #output result
              
       
except (ValueError, IndexError):
    print("Error: Invalid data! Enter a valid data")
        




