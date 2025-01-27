matrix = [
    [3, 7, 1],
    [8, 5, 2],
    [6, 4, 9]]

def diagonal_sum(matrix):
    total = 0

    n = len(matrix)
    for i in range(n):
        total =+ matrix[i][i] 
        return total 
    

print("The main diagonal sum is:", diagonal_sum(matrix))  