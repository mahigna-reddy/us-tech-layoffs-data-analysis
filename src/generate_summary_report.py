import pandas as pd


CLEANED_FILE_PATH = "data/cleaned/cleaned_layoffs.csv"
REPORT_FILE_PATH = "reports/layoffs_summary_report.txt"


def load_cleaned_data(file_path):
    """Load cleaned layoffs dataset and prepare columns for reporting."""
    df = pd.read_csv(file_path)

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    if "total_laid_off" in df.columns:
        df["total_laid_off"] = pd.to_numeric(df["total_laid_off"], errors="coerce")

    return df


def generate_summary_report(df):
    """Generate a business summary report from layoffs dataset."""

    total_layoffs = int(df["total_laid_off"].sum())
    total_companies = df["company"].nunique()
    total_industries = df["industry"].nunique()
    date_range_start = df["date"].min().date()
    date_range_end = df["date"].max().date()

    top_companies = (
        df.groupby("company")["total_laid_off"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    top_industries = (
        df.groupby("industry")["total_laid_off"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    top_locations = (
        df.groupby("location")["total_laid_off"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    report = []
    report.append("US TECH LAYOFFS DATA ANALYSIS SUMMARY REPORT")
    report.append("=" * 55)
    report.append("")
    report.append(f"Total layoffs recorded: {total_layoffs:,}")
    report.append(f"Total unique companies: {total_companies}")
    report.append(f"Total industries impacted: {total_industries}")
    report.append(f"Date range: {date_range_start} to {date_range_end}")
    report.append("")
    report.append("Top 5 companies by layoffs:")
    for company, layoffs in top_companies.items():
        report.append(f"- {company}: {int(layoffs):,}")
    report.append("")
    report.append("Top 5 industries by layoffs:")
    for industry, layoffs in top_industries.items():
        report.append(f"- {industry}: {int(layoffs):,}")
    report.append("")
    report.append("Top 5 locations by layoffs:")
    for location, layoffs in top_locations.items():
        report.append(f"- {location}: {int(layoffs):,}")
    report.append("")
    report.append("Business observations:")
    report.append("- Layoffs were concentrated among large technology companies and consumer-facing industries.")
    report.append("- The dataset shows significant impact across multiple industries and locations.")
    report.append("- Data quality validation was performed before analysis to identify duplicates, missing values, and invalid records.")
    report.append("- Cleaned data was used for analysis to improve reliability of insights.")
    report.append("")
    report.append("Report generated from cleaned layoffs dataset.")

    return "\n".join(report)


def save_report(report_text, file_path):
    """Save summary report to text file."""
    with open(file_path, "w") as file:
        file.write(report_text)

    print(f"Summary report saved to: {file_path}")


if __name__ == "__main__":
    layoffs_df = load_cleaned_data(CLEANED_FILE_PATH)
    summary_report = generate_summary_report(layoffs_df)
    save_report(summary_report, REPORT_FILE_PATH)