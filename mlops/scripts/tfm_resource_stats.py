# Merge members and engagements
# Filter only active engagement, ie engagements with no end date
# Onsite resources are those with a location NOT 'Remote'
# Single-contract Offshore are those with a location 'Remote' and only 1 active engagement
# Multi-contract Offshore are those with a location 'Remote' and more than 1 active engagement
# Shadow are those who has model 'Shadow'
# Trainee are those of type 'Trainee'
# Bench are those who dont fall in any of the above categories

from pandas import read_csv, concat, DataFrame

# Read members and engagements
engagements_df = read_csv("mlops/data/cleaned_engagements.csv")
members_df = read_csv("mlops/data/cleaned_members.csv")
trainings_df = read_csv("mlops/data/cleaned_trainings.csv")

active_engagements_df = engagements_df[engagements_df['End Date'].isnull()]
active_trainings_df = trainings_df[trainings_df['End Date'].isnull()]
# active_engagements_df.to_csv("artifacts/active_engagements.csv", index=False)
# print(active_engagements_df.head())

onsite_engagements_df = active_engagements_df[active_engagements_df['Location'] != 'Remote']
remote_front_engagements_df = active_engagements_df[(active_engagements_df['Location'] == 'Remote') & (~active_engagements_df['Model'].str.contains('Shadow'))]
single_engagements_df = remote_front_engagements_df.groupby('Resource').filter(lambda x: len(x) == 1)
multi_engagements_df = remote_front_engagements_df.groupby('Resource').filter(lambda x: len(x) > 1)
shadow_engagements_df = active_engagements_df[active_engagements_df['Model'].str.contains('Shadow')]

print(shadow_engagements_df.head())
categorized_resources = set(
    concat([
        onsite_engagements_df["Resource"],
        single_engagements_df["Resource"],
        multi_engagements_df["Resource"],
        shadow_engagements_df["Resource"],
        active_trainings_df["Participants"]
    ], ignore_index=True)
)

all_resources = set(members_df["Members"])

bench_resources = all_resources - categorized_resources

summary_df = DataFrame({
    "Type": ["Onsite", "Single Offshore", "Multiple Offshore", "Shadow", "Training", "Bench"],
    "Count": [len(onsite_engagements_df), len(single_engagements_df), len(multi_engagements_df), len(shadow_engagements_df), len(active_trainings_df), len(bench_resources)],
    "Names": [", ".join(onsite_engagements_df["Resource"]), ", ".join(single_engagements_df["Resource"]), ", ".join(multi_engagements_df["Resource"].drop_duplicates(ignore_index=True)), ", ".join(shadow_engagements_df["Resource"] + " (" + shadow_engagements_df["Model"].str.extract(r'\((.*?)\)')[0] + ")"), ", ".join(active_trainings_df["Participants"]), ", ".join(bench_resources)]
})
print(summary_df)
summary_df.to_csv("mlops/artifacts/resource_summary.csv", index=False)