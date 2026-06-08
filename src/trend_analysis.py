import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


CLEANED_FILE_PATH = "data/cleaned/cleaned_layoffs.csv"
VISUALS_PATH = "visuals/"


def load_cleaned_data(file_path):
    """Load cleaned layoffs dataset and prepare columns for trend analysis."""
    df = pd.read_csv(file_path)

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["total_laid_off"] = pd.to_numeric(df["total_laid_off"], errors="coerce")

    return df


def industry_layoffs_by_year(df):
    """Generate yearly layoffs trend for top industries."""

    top_industries = (
        df.groupby("industry")["total_laid_off"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .index
    )

    filtered_df = df[df["industry"].isin(top_industries)]

    trend_data = (
        filtered_df.groupby(["year", "industry"])["total_laid_off"]
        .sum()
        .reset_index()
    )

    plt.figure(figsize=(12, 6))
    sns.lineplot(
        data=trend_data,
        x="year",
        y="total_laid_off",
        hue="industry",
        marker="o"
    )
    plt.title("Layoffs Trend by Top Industries")
    plt.xlabel("Year")
    plt.ylabel("Total Layoffs")
    plt.tight_layout()
    plt.savefig(VISUALS_PATH + "industry_layoffs_by_year.png")
    plt.close()


def location_layoffs_by_year(df):
    """Generate yearly layoffs trend for top locations."""

    top_locations = (
        df.groupby("location")["total_laid_off"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .index
    )

    filtered_df = df[df["location"].isin(top_locations)]

    trend_data = (
        filtered_df.groupby(["year", "location"])["total_laid_off"]
        .sum()
        .reset_index()
    )

    plt.figure(figsize=(12, 6))
    sns.lineplot(
        data=trend_data,
        x="year",
        y="total_laid_off",
        hue="location",
        marker="o"
    )
    plt.title("Layoffs Trend by Top Locations")
    plt.xlabel("Year")
    plt.ylabel("Total Layoffs")
    plt.tight_layout()
    plt.savefig(VISUALS_PATH + "location_layoffs_by_year.png")
    plt.close()


def monthly_layoffs_trend(df):
    """Generate monthly layoffs trend."""

    monthly_data = (
        df.groupby("year_month")["total_laid_off"]
        .sum()
        .reset_index()
        .sort_values("year_month")
    )

    plt.figure(figsize=(14, 6))
    sns.lineplot(
        data=monthly_data,
        x="year_month",
        y="total_laid_off",
        marker="o"
    )
    plt.title("Monthly Layoffs Trend")
    plt.xlabel("Year-Month")
    plt.ylabel("Total Layoffs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(VISUALS_PATH + "monthly_layoffs_trend.png")
    plt.close()


def print_trend_summary(df):
    """Print summary of trend analysis."""

    print("========== TREND ANALYSIS SUMMARY ==========")

    highest_year = (
        df.groupby("year")["total_laid_off"]
        .sum()
        .sort_values(ascending=False)
        .head(1)
    )

    highest_month = (
        df.groupby("year_month")["total_laid_off"]
        .sum()
        .sort_values(ascending=False)
        .head(1)
    )

    print("\nYear with highest layoffs:")
    print(highest_year)

    print("\nMonth with highest layoffs:")
    print(highest_month)

    print("\nTop 5 industries by layoffs:")
    print(
        df.groupby("industry")["total_laid_off"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    print("\nTop 5 locations by layoffs:")
    print(
        df.groupby("location")["total_laid_off"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    print("\n========== TREND ANALYSIS COMPLETED ==========")


if __name__ == "__main__":
    layoffs_df = load_cleaned_data(CLEANED_FILE_PATH)

    print_trend_summary(layoffs_df)

    industry_layoffs_by_year(layoffs_df)
    location_layoffs_by_year(layoffs_df)
    monthly_layoffs_trend(layoffs_df)

    print("Trend analysis charts saved successfully in visuals folder.")