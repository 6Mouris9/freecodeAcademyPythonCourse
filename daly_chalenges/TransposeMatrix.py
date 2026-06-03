def print_matrix_2d(matrix):
    for line in matrix:
        print(line)

def transpose(matrix):
    lines = len(matrix)
    columns = len(matrix[0])
    print(f"Entry matrix:\nLines: {lines} | Columns: {columns}")
    print_matrix_2d(matrix)
    print(f"Out Matrix:\nLines: {columns} | Columns: {lines}")
    
    # making a matrix
    new_matrix = []
    for i in range(0, columns):
        new_line = []
        for j in range(0, lines):
            new_line.append(matrix[j][i])
        new_matrix.append(new_line)
    
    print_matrix_2d(new_matrix)

    matrix = new_matrix
    return matrix


# new matrix = col to->line
matrix = [  [1,2,3],
            [3,4,5],
            [6,7,8],
            [1,23,4]]

transpose(matrix)
