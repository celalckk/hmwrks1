# example matrix 
matrix = [
    [3, 7, 1],
    [8, 5, 2],
    [6, 4, 9]
]

# Function to calculate the sum of all elements in the matrix 
def sum_matrix_elements(matrix):
    total_sum = 0
    for row in matrix:
        for element in row:
            total_sum += element
    return total_sum

# Calculate the sum and print 
total_sum = sum_matrix_elements(matrix)
print("the matrix theme is the sum off all elements:" , total_sum)


  
