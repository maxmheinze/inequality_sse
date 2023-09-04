########################################################################
############################# ASSIGNMENT 1 #############################
################################ Task 2 ################################
########################################################################

# %% Importing Libraries etc.

import os
import numpy as np 

os.chdir("/Users/heinzemax/Documents/GitHub/inequality_sse/assignment_1")


# %% Problem 2.1

# Creating the matrix
our_matrix = np.array(
        [
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
        ]
    )

# Creating the vector
our_vector = np.array([10,20,30])

# Adding the vector to each column
result_matrix_21 = our_matrix + our_vector[:, np.newaxis]


# %% Problem 2.2

# Creating the function as specified in the assignment
def add_vector_columnwise(input_matrix, input_vector):

  if input_matrix.shape[0] == input_vector.shape[0] :
    return input_matrix + input_vector[:, np.newaxis]

  else :
    raise ValueError("Length of vector and number of rows of matrix must coincide!") 

# Create a vector that will throw an error
our_error_vector = np.array([10, 20, 30, 40])

# Use the function with appropriate inputs
result_matrix_22 = add_vector_columnwise(our_matrix, our_vector)

# Use the function with inappropriate inputs
try:
    add_vector_columnwise(our_matrix, our_error_vector)
except ValueError as e:
    print(f"Error encountered: {e}")


# %% Problem 2.3

# Creating the function as specified in the assignment
def check_matrices_equal(matrix_1, matrix_2) :
    
    # Check whether the dimensions match. If not, return false
    if matrix_1.shape[0] != matrix_2.shape[0] or matrix_1.shape[1] != matrix_2.shape[1]:
        return False
    
    # Check whether the elements match. If not, return false
    for i in range(matrix_1.shape[0]):
        for j in range(matrix_1.shape[1]):
            if matrix_1[i][j] != matrix_2[i][j]:
                return False
    
    # Otherwise, return true
    return True

# Apply the function to check whether the matrices are the same
print("\nProblem 2.3: Matrix equality check")
print(check_matrices_equal(result_matrix_21, result_matrix_22))
        
        
# %% Problem 2.4

# Creating the class as specified in the assignment
class matrix_mod:
    def __init__(self, input_matrix):
        self.matrix = input_matrix
    def modify(self, input_vector):
        self.matrix = add_vector_columnwise(self.matrix, input_vector)
        
# Performing the modification
result_matrix_24 = matrix_mod(our_matrix)
result_matrix_24.modify(our_vector)

# Checking equality
print("\nProblem 2.4: Matrix equality check")
print(check_matrices_equal(result_matrix_21, result_matrix_24.matrix))















 