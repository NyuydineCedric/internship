#MATRIX OPERATION

def transpose(matrix):
    
    result = []
 
    for column in range(len(matrix[0])):
        new_row = []

        for row in range(len(matrix)):
            new_row.append(matrix[row][column])

        result.append(new_row)

    return result


def matrix_sum(matrix):

    total = 0

    for row in matrix:
        for number in row:
            total = total + number

    return total


def row_with_max_sum(matrix):

    max_sum = 0
    max_index = 0

    for i in range(len(matrix)):
        total = 0

        for number in matrix[i]:
            total = total + number

        if i == 0:
            max_sum = total
            max_index = i
        elif total > max_sum:
            max_sum = total
            max_index = i

    return max_index


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(transpose(matrix))
print(matrix_sum(matrix))
print(row_with_max_sum(matrix))