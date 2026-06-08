import pandas as pd


RAW_FILE_PATH = "data/raw/layoffs.csv"


def load_data(file_path):
    """Load layoffs CSV file."""
    return pd.read_csv(file_path)


def run_data_quality_checks(df):
    """Run basic data quality checks on the layoffs dataset."""

    print("========== DATA QUALITY CHECKS ==========")

    print("\n1. Dataset shape:")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\n2. Column names:")
    print(df.columns.tolist())

    print("\n3. Missing values by column:")
    print(df.isnull().sum())

    print("\n4. Duplicate records:")
    print(df.duplicated().sum())

    print("\n5. Invalid total_laid_off values:")
    if "total_laid_off" in df.columns:
        invalid_layoffs = df[df["total_laid_off"] < 0]
        print(len(invalid_layoffs))
    else:
        print("Column total_laid_off not found")

    print("\n6. Invalid percentage_laid_off values:")
    if "percentage_laid_off" in df.columns:
        invalid_percentage = df[
            (df["percentage_laid_off"] < 0) | (df["percentage_laid_off"] > 1)
            ]
        print(len(invalid_percentage))
    else:
        print("Column percentage_laid_off not found")

    print("\n7. Date column check:")
    if "date" in df.columns:
        converted_dates = pd.to_datetime(df["date"], errors="coerce")
        invalid_dates = converted_dates.isnull().sum()
        print(f"Invalid or missing dates: {invalid_dates}")
    else:
        print("Column date not found")

    print("\n========== CHECKS COMPLETED ==========")


if __name__ == "__main__":
    layoffs_df = load_data(RAW_FILE_PATH)
    run_data_quality_checks(layoffs_df)