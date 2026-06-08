import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


CLEANED_FILE_PATH = "data/cleaned/cleaned_layoffs.csv"
VISUALS_PATH = "visuals/"


def load_cleaned_data(file_path):
    """Load cleaned layoffs dataset and prepare columns for analysis."""
    df = pd.read_csv(file_path)

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    if "total_laid_off" in df.columns:
        df["total_laid_off"] = pd.to_numeric(df["total_laid_off"], errors="coerce")

    if "funds_raised_millions" in df.columns:
        df["funds_raised_millions"] = pd.to_numeric(df["funds_raised_millions"], errors="coerce")

    return df


def top_companies_by_layoffs(df):
    """Generate chart for top companies by total layoffs."""

    top_companies = (
        df.groupby("company")["total_laid_off"]
        .sum()
        .dropna()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_companies.values, y=top_companies.index)
    plt.title("Top 10 Companies by Total Layoffs")
    plt.xlabel("Total Layoffs")
    plt.ylabel("Company")
    plt.tight_layout()
    plt.savefig(VISUALS_PATH + "top_companies_by_layoffs.png")
    plt.close()


def top_industries_by_layoffs(df):
    """Generate chart for top industries by total layoffs."""

    top_industries = (
        df.groupby("industry")["total_laid_off"]
        .sum()
        .dropna()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_industries.values, y=top_industries.index)
    plt.title("Top 10 Industries by Total Layoffs")
    plt.xlabel("Total Layoffs")
    plt.ylabel("Industry")
    plt.tight_layout()
    plt.savefig(VISUALS_PATH + "top_industries_by_layoffs.png")
    plt.close()


def layoffs_trend_by_year(df):
    """Generate chart for layoffs trend by year."""

    yearly_layoffs = (
        df.groupby("year")["total_laid_off"]
        .sum()
        .dropna()
        .sort_index()
    )

    plt.figure(figsize=(10, 5))
    sns.lineplot(x=yearly_layoffs.index, y=yearly_layoffs.values, marker="o")
    plt.title("Layoffs Trend by Year")
    plt.xlabel("Year")
    plt.ylabel("Total Layoffs")
    plt.tight_layout()
    plt.savefig(VISUALS_PATH + "layoffs_trend_by_year.png")
    plt.close()


def top_locations_by_layoffs(df):
    """Generate chart for top locations by total layoffs."""

    top_locations = (
        df.groupby("location")["total_laid_off"]
        .sum()
        .dropna()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_locations.values, y=top_locations.index)
    plt.title("Top 10 Locations by Total Layoffs")
    plt.xlabel("Total Layoffs")
    plt.ylabel("Location")
    plt.tight_layout()
    plt.savefig(VISUALS_PATH + "top_locations_by_layoffs.png")
    plt.close()


def print_business_insights(df):
    """Print business-level insights from the layoffs dataset."""

    print("========== BUSINESS INSIGHTS ==========")

    total_layoffs = df["total_laid_off"].sum()
    total_companies = df["company"].nunique()
    total_industries = df["industry"].nunique()
    date_range_start = df["date"].min().date()
    date_range_end = df["date"].max().date()

    print(f"Total layoffs recorded: {int(total_layoffs)}")
    print(f"Total unique companies: {total_companies}")
    print(f"Total industries impacted: {total_industries}")
    print(f"Date range: {date_range_start} to {date_range_end}")

    print("\nTop 5 companies by layoffs:")
    print(df.groupby("company")["total_laid_off"].sum().sort_values(ascending=False).head(5))

    print("\nTop 5 industries by layoffs:")
    print(df.groupby("industry")["total_laid_off"].sum().sort_values(ascending=False).head(5))

    print("\n========== ANALYSIS COMPLETED ==========")


if __name__ == "__main__":
    layoffs_df = load_cleaned_data(CLEANED_FILE_PATH)

    print_business_insights(layoffs_df)

    top_companies_by_layoffs(layoffs_df)
    top_industries_by_layoffs(layoffs_df)
    layoffs_trend_by_year(layoffs_df)
    top_locations_by_layoffs(layoffs_df)

    print("Charts saved successfully in visuals folder.")