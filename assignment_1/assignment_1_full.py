########################################################################
############################# ASSIGNMENT 1 #############################
########################################################################

# Group 3:
# Lourdes Gutiérrez De San Miguel, 
# Max Heinze, 
# Gustav Pirich, 
# Berk Uzunonat;
# September 5, 2023



########################################################################
################################ Task 1 ################################
########################################################################


# %% Importing Libraries

import os
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# %% Problem 1.1

# !!! CHANGE THE FOLLOWING LINE TO MAKE THE CODE WORK ON YOUR DEVICE !!!

# Changing the working directory
os.chdir("/Users/heinzemax/Documents/GitHub/inequality_sse/assignment_1")

# Reading in the data
income_data = pd.read_stata("psid1999.dta")

# Filtering the data so that only household heads are contained.
# Note that filtering by relationhead==10 is kind of a "best guess" after
# consulting PSID codebooks available online, since the variable in question 
# is not labeled. Source for the "best guess": Page 4 of the document available at
# https://psidonline.isr.umich.edu/documents/psid/codebook/MX19REL_codebook.pdf
income_data = income_data.query("relationhead == 10")

# %% Problem 1.2

# Filtering the data set by age older than 24 and younger than 66
income_data = income_data.query("age > 24 & age < 66")

# Filtering the data set by married HHH with spouse present
income_data = income_data.query("(mls=='married' & sp_in_fu=='Spouse/Partner in FU now')")


# %% Problem 1.3

# Filtering out all household heads who worked zero hours
income_data = income_data.query("head_hrs > 0")

# Creating a logged hourly earnings variable from yearly income and yearly hrs, 
# adding 1 to avoid taking the log of 0
income_data['log_hr_earnings'] = np.log((income_data['head_li'] / income_data['head_hrs']) + 1)

# Computing averages by age and education
average_wages = income_data.groupby(['age', 'edu'])['log_hr_earnings'].mean().reset_index()


# %% Problem 1.4

# Create a scatter plot showing avg log hrly earnings by age, with education
# levels represented as different colored dots
plt.figure(figsize=(8,6), dpi = 300)

education_levels = average_wages['edu'].unique()

for this_education_level in education_levels:
    subset = average_wages[average_wages['edu'] == this_education_level]
    plt.scatter(subset['age'], subset['log_hr_earnings'], label=this_education_level)

plt.title('Average Log Hourly Earnings by Age and Education')
plt.xlabel('Age')
plt.ylabel('Average Log Hourly Earnings')
plt.legend(title = "Education")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()



########################################################################
################################ Task 2 ################################
########################################################################


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

