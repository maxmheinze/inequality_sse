########################################################################
############################# ASSIGNMENT 1 #############################
################################ Task 1 ################################
########################################################################

# %% Importing Libraries

import os
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# %% Problem 1.1

# Changing the working directory
os.chdir("/Users/heinzemax/Documents/GitHub/inequality_sse/assignment_1")

# Reading in the data
income_data = pd.read_stata("/Users/heinzemax/Documents/GitHub/inequality_sse/assignment_1/psid1999.dta")

# Filtering the data so that only household heads are contained.
# Note that filtering by relationhead==10 is kind of a "best guess" after
# consulting PSID codebooks available online, since no proper documentation
# was provided with the dataset and the variable in question is not labeled.
# Source for the "best guess": Page 4 of the document available at
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

# Replacing all zero values with 0.1 in order to avoid infinite logs
income_data['head_li'] = income_data['head_li'].replace(0, 0.1)

# Creating a logged hourly earnings variable from yearly income and yearly hrs
income_data['log_hr_earnings'] = np.log(income_data['head_li'] / income_data['head_hrs'])

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


