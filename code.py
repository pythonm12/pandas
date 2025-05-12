import pandas as pd

# Load the dataset
df = pd.read_csv("path")

# 1. How many men and women (sex feature) are represented in this dataset?
gender_count = df['gender'].value_counts()
print("Number of men and women:\n", gender_count)

# 2. What is the average age (age feature) of women?
average_age_women = df[df['gender'] == 'Female']['age'].mean()
print(f"Average age of women: {average_age_women:.2f}")

# 3. What is the percentage of German citizens (native-country feature)?
german_percentage = (df[df['native-country'] == 'Germany'].shape[0] / df.shape[0]) * 100
print(f"Percentage of German citizens: {german_percentage:.2f}%")

# 4. Mean and standard deviation of age for those who earn more than 50K per year and less than 50K per year
high_income = df[df['income'] == '>50K']
low_income = df[df['income'] == '<=50K']
high_income_age_mean = high_income['age'].mean()
high_income_age_std = high_income['age'].std()
low_income_age_mean = low_income['age'].mean()
low_income_age_std = low_income['age'].std()

print(f"\nFor those earning >50K:\nMean Age: {high_income_age_mean:.2f}, Standard Deviation: {high_income_age_std:.2f}")
print(f"For those earning <=50K:\nMean Age: {low_income_age_mean:.2f}, Standard Deviation: {low_income_age_std:.2f}")

# 5. People earning more than 50K have at least high school education?
high_school_education = ['Bachelors', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', 'Masters', 'Doctorate']
high_income_education = high_income[high_income['education'].isin(high_school_education)]
if high_income_education.shape[0] == high_income.shape[0]:
    print("\nAll people earning >50K have at least high school education.")
else:
    print("\nNot all people earning >50K have at least high school education.")

# 6. Age statistics for each race and each gender
age_stats_by_race_gender = df.groupby(['race', 'gender'])['age'].describe()
print("\nAge statistics by race and gender:\n", age_stats_by_race_gender)

# Maximum age of men of Amer-Indian-Eskimo race
max_age_amer_indian_eskimo = df[(df['race'] == 'Amer-Indian-Eskimo') & (df['gender'] == 'Male')]['age'].max()
print(f"\nMaximum age of men of Amer-Indian-Eskimo race: {max_age_amer_indian_eskimo}")

# 7. Proportion of those who earn a lot (>50K) among married or single men
df['is_married'] = df['marital-status'].str.startswith('Married')
married_men = df[(df['gender'] == 'Male') & (df['is_married'] == True)]
married_men_proportion = (married_men['income'] == '>50K').mean()
single_men = df[(df['gender'] == 'Male') & (df['is_married'] == False)]
single_men_proportion = (single_men['income'] == '>50K').mean()

print(f"\nProportion of married men earning >50K: {married_men_proportion:.2f}")
print(f"Proportion of single men earning >50K: {single_men_proportion:.2f}")

# 8. Maximum number of hours worked per week
max_hours_per_week = df['hours-per-week'].max()
print(f"Maximum number of hours worked per week: {max_hours_per_week}")

# 9. People working the maximum hours per week and the percentage of those earning >50K
people_work_max_hours = df[df['hours-per-week'] == max_hours_per_week]
percentage_earning_above_50k = (people_work_max_hours['income'] == '>50K').mean() * 100
print(f"\nPeople working {max_hours_per_week} hours per week: {people_work_max_hours.shape[0]}")
print(f"Percentage of those earning >50K: {percentage_earning_above_50k:.2f}%")

# 10. Average work hours per week by country and salary for Japan
avg_work_hours_by_country = df.groupby(['native-country', 'income'])['hours-per-week'].mean()
avg_work_hours_japan = avg_work_hours_by_country.get(('Japan', '>50K'), None), avg_work_hours_by_country.get(('Japan', '<=50K'), None)
print(f"\nAverage work hours per week in Japan for people earning >50K and <=50K: {avg_work_hours_japan}")
