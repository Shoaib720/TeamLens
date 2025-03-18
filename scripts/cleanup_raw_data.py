# This script will perform the following:
# 1. Forward fill merged columns
# 2. Address null fields

import pandas as pd

# Load the CSV file
# file_path = ".data/engagements.csv"  # Replace with your actual CSV file path
engagements_df = pd.read_csv(".data/engagements.csv")
members_df = pd.read_csv(".data/members.csv")
trainings_df = pd.read_csv(".data/trainings.csv")


# ===== Engagements =========
# Forward-fill the 'Resource' column to handle merged cells
engagements_df['Resource'] = engagements_df['Resource'].fillna(method='ffill')
engagements_df['Location'] = engagements_df['Location'].fillna("Onsite")
engagements_df['Experience'] = engagements_df['Experience'].fillna("4+")

# ===== Trainings =========
trainings_df['Program Name'] = trainings_df['Program Name'].fillna(method='ffill')
trainings_df['Start Date'] = trainings_df['Start Date'].fillna(method='ffill')
trainings_df['End Date'] = trainings_df['End Date'].fillna(method='ffill')
trainings_df['Trainers'] = trainings_df['Trainers'].fillna(method='ffill')

# ===== Members =========
# No cleanup yet

# Save cleaned CSV (optional)
engagements_df.to_csv("artifacts/cleaned_engagements.csv", index=False)
trainings_df.to_csv("artifacts/cleaned_trainings.csv", index=False)

# Print first few rows for verification
print(engagements_df.head())
print(trainings_df.head())

# def fill_missing_values(df, fill_map):
#     """
#     Fills missing (NaN) values in specified columns with default values.

#     Parameters:
#     df (pd.DataFrame): The DataFrame to modify.
#     fill_map (dict): Dictionary where keys are column names and values are default values.

#     Returns:
#     pd.DataFrame: Modified DataFrame with filled values.
#     """
#     for column, default_value in fill_map.items():
#         df[column] = df[column].fillna(default_value)
#     return df

