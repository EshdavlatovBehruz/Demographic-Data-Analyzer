import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.csv")

    df.columns = df.columns.str.strip()
    df["salary"] = df["salary"].str.strip()
    df["native-country"] = df["native-country"].str.strip()
    df["education"] = df["education"].str.strip()

    race = df["race"].value_counts()

    avg_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    percent = round((df["education"] == "Bachelors").sum() / len(df) * 100, 1)

    high_edu = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    loss_edu = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    high_edu_rich = round((high_edu["salary"] == ">50K").sum() / len(high_edu) * 100, 1)
    loss_edu_rich = round((loss_edu["salary"] == ">50K").sum() / len(loss_edu) * 100, 1)

    work_hours = df["hours-per-week"].min()

    num_workers = df[df["hours-per-week"] == work_hours]
    rich = round((num_workers["salary"] == ">50K").sum() / len(num_workers) * 100, 1)

    country_salary = df.groupby("native-country")["salary"].value_counts(normalize=True).unstack().fillna(0)
    high_earn_country = country_salary[">50K"].idxmax()
    high_earn_country_percent = round(country_salary[">50K"].max() * 100, 1)

    india_rich = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    top_occupa = india_rich["occupation"].value_counts().idxmax() if not india_rich.empty else "No Data"

    if print_data:
        print("Number of each race:\n", race)
        print("Average age of men:", avg_men)
        print(f"Percentage with Bachelors degrees: {percent}%")
        print(f"Percentage with higher education that earn >50K: {high_edu_rich}%")
        print(f"Percentage without higher education that earn >50K: {loss_edu_rich}%")
        print(f"Min work time: {work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich}%")
        print("Country with highest percentage of rich:", high_earn_country)
        print(f"Highest percentage of rich people in country: {high_earn_country_percent}%")
        print("Top occupations in India:", top_occupa)

    return {
        'race_count': race,
        'average_age_men': avg_men,
        'percentage_bachelors': percent,
        'higher_education_rich': high_edu_rich,
        'lower_education_rich': loss_edu_rich,
        'min_work_hours': work_hours,
        'rich_percentage': rich,
        'highest_earning_country': high_earn_country,
        'highest_earning_country_percentage': high_earn_country_percent,
        'top_IN_occupation': top_occupa
    }
