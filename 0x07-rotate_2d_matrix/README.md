# Rotate 2-D Matrix

## Tasks
+ 0. **Rotate 2D Matrix**

- Given an n x n 2D matrix, rotate it 90 degrees clockwise.

- Prototype: def rotate_2d_matrix(matrix):
- Do not return anything. The matrix must be edited in-place.
- You can assume the matrix will have 2 dimensions and will not be empty.

- [0-rotate_2d_matrix.py](./0-rotate_2d_matrix.py)

- The function takes a 2D matrix as input and modifies it in-place. It first calculates the size of the matrix (assuming it's square), then transposes the matrix using a nested loop. The matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] line swaps the elements in the i-th row and j-th column with the elements in the j-th row and i-th column, effectively swapping the rows and columns.

- After the transpose, the function then reverses each row of the matrix using the matrix[i][::-1] slicing notation, which creates a reversed copy of the i-th row and assigns it back to the original row.

- Finally, the function does not return anything, but modifies the input matrix in-place, which means the original matrix will be rotated 90 degrees clockwise after the function call.
