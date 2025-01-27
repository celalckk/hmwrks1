# Example matrix
matrix = [
    [3, 7, 1],
    [8, 5, 2],
    [6, 4, 9]
]

# Function to find the minimum element in the matrix
def find_min_element(matrix):
    min_element = matrix[0][0]  # Initialize with the first element
    for row in matrix:
        for element in row:
            if element < min_element:
                min_element = element
    return min_element

# Find and print the minimum element
min_element = find_min_element(matrix)
print("The minimum element in the matrix is:", min_element)  
