import pandas as pd


RAW_FILE_PATH = "data/raw/layoffs.csv"
CLEANED_FILE_PATH = "data/cleaned/cleaned_layoffs.csv"


def load_data(file_path):
    """Load raw layoffs dataset."""
    return pd.read_csv(file_path)


def clean_layoffs_data(df):
    """Clean layoffs dataset for analysis."""

    print("========== DATA CLEANING STARTED ==========")

    print(f"Original rows: {df.shape[0]}")
    print(f"Original columns: {df.shape[1]}")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Standardize text columns
    text_columns = ["company", "location", "industry", "stage", "country"]

    for column in text_columns:
        if column in df.columns:
            df[column] = df[column].astype(str).str.strip()

    # Convert date column to datetime
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Convert numeric columns
    numeric_columns = ["total_laid_off", "percentage_laid_off", "funds_raised_millions"]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    # Create year and month columns for trend analysis
    if "date" in df.columns:
        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month
        df["year_month"] = df["date"].dt.to_period("M").astype(str)

    print(f"Cleaned rows: {df.shape[0]}")
    print(f"Cleaned columns: {df.shape[1]}")

    print("========== DATA CLEANING COMPLETED ==========")

    return df


def save_cleaned_data(df, file_path):
    """Save cleaned dataset."""
    df.to_csv(file_path, index=False)
    print(f"Cleaned file saved to: {file_path}")


if __name__ == "__main__":
    layoffs_df = load_data(RAW_FILE_PATH)
    cleaned_df = clean_layoffs_data(layoffs_df)
    save_cleaned_data(cleaned_df, CLEANED_FILE_PATH)