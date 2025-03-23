# This script will perform the following:
# 1. Forward fill merged columns
# 2. Address null fields
# 3. Convert date columns to datetime

from pandas import read_csv, to_datetime

# Load the CSV file
engagements_df = read_csv("mlops/data/engagements.csv")
members_df = read_csv("mlops/data/members.csv")
trainings_df = read_csv("mlops/data/trainings.csv")


# ===== Engagements =========
# Forward-fill the 'Resource' column to handle merged cells
engagements_df['Resource'] = engagements_df['Resource'].fillna(method='ffill')
engagements_df['Location'] = engagements_df['Location'].fillna("Onsite")
engagements_df['Experience'] = engagements_df['Experience'].fillna("4+")
engagements_df["Start Date"] = to_datetime(engagements_df["Start Date"], format="%d %b, %Y", errors="coerce")
engagements_df["End Date"] = to_datetime(engagements_df["End Date"], format="%d %b, %Y", errors="coerce")

# ===== Trainings =========
trainings_df['Program Name'] = trainings_df['Program Name'].fillna(method='ffill')
trainings_df['Start Date'] = trainings_df['Start Date'].fillna(method='ffill')
trainings_df['End Date'] = trainings_df['End Date'].fillna(method='ffill')
trainings_df['Trainers'] = trainings_df['Trainers'].fillna(method='ffill')
trainings_df["Start Date"] = to_datetime(trainings_df["Start Date"], format="%d %b, %Y", errors="coerce")
trainings_df["End Date"] = to_datetime(trainings_df["End Date"], format="%d %b, %Y", errors="coerce")


# ===== Members =========
# No cleanup yet
members_df["DoJ"] = to_datetime(members_df["DoJ"], format="%d %b, %Y", errors="coerce")
members_df["Committed till"] = to_datetime(members_df["Committed till"], format="%b, %Y", errors="coerce")

# Save cleaned CSV (optional)
engagements_df.to_csv("mlops/artifacts/cleaned_engagements.csv", index=False)
trainings_df.to_csv("mlops/artifacts/cleaned_trainings.csv", index=False)
members_df.to_csv("mlops/artifacts/cleaned_members.csv", index=False)

# Print first few rows for verification
print(engagements_df.head())
print(trainings_df.head())
print(members_df.head())

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

