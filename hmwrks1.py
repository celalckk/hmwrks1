# Example matrix
matrix = [
    [3, 7, 1],
    [8, 5, 2],
    [6, 4, 9]
]

# Target value to search for
target_value = 2

# Function to find all indices of the target value in the matrix
def find_target_indices(matrix, target_value):
    indices = []
    for row_index, row in enumerate(matrix):
        for col_index, element in enumerate(row):
            if element == target_value:
                indices.append((row_index, col_index))
    return indices

# Find and print the indices of the target value
target_indices = find_target_indices(matrix, target_value)
print("The indices of the target value in the matrix are:", target_indices)






def uniqe_elements(matrix):
    uniqe_set = set()
    for row in matrix:
        for element in row:
            uniqe_set.add(element)

    return list(uniqe_set)
matrix = [
    [3, 7, 1],
    [8, 5, 2],
    [6, 4, 9]
]

print("unique elements:", uniqe_elements(matrix))



def secondary_elements(matrix):
    total = 0 
    n = len(matrix)
    for i in range(n):
        total +=  matrix[i][n-i-1]
        return total 
    
matrix = [
    [3, 7, 1],
    [8, 5, 2],
    [6, 4, 9]
]
    
print("the second diogonal sum is:" , secondary_elements(matrix)) 