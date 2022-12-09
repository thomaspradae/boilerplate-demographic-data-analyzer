from statistics import mean
import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    mean_age = df.loc[df['sex'] == 'Male','age']
    average_age_men = round(mean_age.mean(), 1) 

    # What is the percentage of people who have a Bachelor's degree?
    perbachelors =  df['education'].value_counts(normalize=True)
    percentage_bachelors = round((perbachelors.Bachelors)*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced_education = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    higher_education_rich = round(((advanced_education['salary'].value_counts(normalize=True)['>50K'])*100),1)

    # What percentage of people without advanced education make more than 50K?
    lower_ed = df[~df.education.isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = round((lower_ed['salary'].value_counts(normalize=True)[">50K"]*100),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    rich_percentage = round((df[df['hours-per-week'] == min_work_hours]['salary'].value_counts(normalize=True)['>50K']*100),1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = round((df.loc[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()) * 100, 1).sort_values(ascending=False).keys()[0]
    highest_earning_country_percentage = round(((df.loc[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts())*100),1).max()

    # Identify the most popular occupation for those who earn >50K in India.
    india_df = df[df['native-country'] == 'India']
    india_over_50k = india_df[df['salary'] == '>50K']
    top_IN_occupation = india_over_50k['occupation'].value_counts().keys()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data(print_data=True)