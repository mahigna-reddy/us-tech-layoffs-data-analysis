import os
import pandas as pd


RAW_FILE_PATH = "data/raw/layoffs.csv"
CLEANED_FILE_PATH = "data/cleaned/cleaned_layoffs.csv"
REPORT_FILE_PATH = "reports/data_validation_report.txt"


REQUIRED_COLUMNS = [
    "company",
    "location",
    "industry",
    "total_laid_off",
    "percentage_laid_off",
    "date",
    "stage",
    "country",
    "funds_raised_millions"
]


def load_data(file_path):
    """Load CSV data."""
    return pd.read_csv(file_path)


def add_result(results, status, check_name, details):
    """Add validation result to report list."""
    results.append({
        "status": status,
        "check_name": check_name,
        "details": details
    })


def validate_required_columns(df, results):
    """Validate that all required columns exist."""
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]

    if missing_columns:
        add_result(
            results,
            "FAIL",
            "Required columns validation",
            f"Missing required columns: {missing_columns}"
        )
    else:
        add_result(
            results,
            "PASS",
            "Required columns validation",
            "All required columns are present."
        )


def validate_duplicate_records(df, results):
    """Validate duplicate records."""
    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        add_result(
            results,
            "WARNING",
            "Duplicate records validation",
            f"Duplicate records found: {duplicate_count}"
        )
    else:
        add_result(
            results,
            "PASS",
            "Duplicate records validation",
            "No duplicate records found."
        )


def validate_missing_values(df, results):
    """Validate missing values by column."""
    missing_values = df.isnull().sum()
    columns_with_missing_values = missing_values[missing_values > 0]

    if columns_with_missing_values.empty:
        add_result(
            results,
            "PASS",
            "Missing values validation",
            "No missing values found."
        )
    else:
        details = []
        for column, count in columns_with_missing_values.items():
            details.append(f"{column}: {count}")

        add_result(
            results,
            "WARNING",
            "Missing values validation",
            "Missing values found - " + ", ".join(details)
        )


def validate_negative_layoff_values(df, results):
    """Validate that total_laid_off does not contain negative values."""
    if "total_laid_off" not in df.columns:
        add_result(
            results,
            "FAIL",
            "Negative layoff values validation",
            "Column total_laid_off not found."
        )
        return

    df["total_laid_off"] = pd.to_numeric(df["total_laid_off"], errors="coerce")
    invalid_count = df[df["total_laid_off"] < 0].shape[0]

    if invalid_count > 0:
        add_result(
            results,
            "FAIL",
            "Negative layoff values validation",
            f"Negative layoff values found: {invalid_count}"
        )
    else:
        add_result(
            results,
            "PASS",
            "Negative layoff values validation",
            "No negative layoff values found."
        )


def validate_percentage_range(df, results):
    """Validate percentage_laid_off values are between 0 and 1."""
    if "percentage_laid_off" not in df.columns:
        add_result(
            results,
            "FAIL",
            "Percentage range validation",
            "Column percentage_laid_off not found."
        )
        return

    df["percentage_laid_off"] = pd.to_numeric(df["percentage_laid_off"], errors="coerce")

    invalid_count = df[
        (df["percentage_laid_off"] < 0) |
        (df["percentage_laid_off"] > 1)
        ].shape[0]

    if invalid_count > 0:
        add_result(
            results,
            "FAIL",
            "Percentage range validation",
            f"Invalid percentage values found: {invalid_count}"
        )
    else:
        add_result(
            results,
            "PASS",
            "Percentage range validation",
            "All percentage values are within valid range."
        )


def validate_date_column(df, results):
    """Validate date column can be converted to datetime."""
    if "date" not in df.columns:
        add_result(
            results,
            "FAIL",
            "Date validation",
            "Column date not found."
        )
        return

    converted_dates = pd.to_datetime(df["date"], errors="coerce")
    invalid_date_count = converted_dates.isnull().sum()

    if invalid_date_count > 0:
        add_result(
            results,
            "WARNING",
            "Date validation",
            f"Invalid or missing dates found: {invalid_date_count}"
        )
    else:
        add_result(
            results,
            "PASS",
            "Date validation",
            "All dates are valid."
        )


def validate_cleaned_file_exists(results):
    """Validate cleaned file was generated."""
    if os.path.exists(CLEANED_FILE_PATH):
        add_result(
            results,
            "PASS",
            "Cleaned file validation",
            "Cleaned dataset file exists."
        )
    else:
        add_result(
            results,
            "FAIL",
            "Cleaned file validation",
            "Cleaned dataset file does not exist."
        )


def validate_visual_files_exist(results):
    """Validate expected visual files were generated."""
    expected_visuals = [
        "visuals/top_companies_by_layoffs.png",
        "visuals/top_industries_by_layoffs.png",
        "visuals/layoffs_trend_by_year.png",
        "visuals/top_locations_by_layoffs.png",
        "visuals/industry_layoffs_by_year.png",
        "visuals/location_layoffs_by_year.png",
        "visuals/monthly_layoffs_trend.png"
    ]

    missing_visuals = [file for file in expected_visuals if not os.path.exists(file)]

    if missing_visuals:
        add_result(
            results,
            "WARNING",
            "Visual files validation",
            f"Missing visual files: {missing_visuals}"
        )
    else:
        add_result(
            results,
            "PASS",
            "Visual files validation",
            "All expected visual files exist."
        )


def generate_validation_report(results):
    """Generate validation report text."""
    report = []

    report.append("DATA VALIDATION REPORT")
    report.append("=" * 50)
    report.append("")

    total_checks = len(results)
    pass_count = len([result for result in results if result["status"] == "PASS"])
    warning_count = len([result for result in results if result["status"] == "WARNING"])
    fail_count = len([result for result in results if result["status"] == "FAIL"])

    report.append(f"Total checks executed: {total_checks}")
    report.append(f"Passed checks: {pass_count}")
    report.append(f"Warnings: {warning_count}")
    report.append(f"Failed checks: {fail_count}")
    report.append("")

    report.append("Validation Results:")
    report.append("-" * 50)

    for result in results:
        report.append(f"{result['status']}: {result['check_name']}")
        report.append(f"Details: {result['details']}")
        report.append("")

    report.append("Report Summary:")
    if fail_count > 0:
        report.append("Some validations failed. Review failed checks before using the dataset for final reporting.")
    elif warning_count > 0:
        report.append("No critical failures found. Warnings were identified and should be reviewed.")
    else:
        report.append("All validations passed successfully.")

    return "\n".join(report)


def save_report(report_text, file_path):
    """Save validation report."""
    with open(file_path, "w") as file:
        file.write(report_text)

    print(f"Data validation report saved to: {file_path}")


if __name__ == "__main__":
    validation_results = []

    raw_df = load_data(RAW_FILE_PATH)

    validate_required_columns(raw_df, validation_results)
    validate_duplicate_records(raw_df, validation_results)
    validate_missing_values(raw_df, validation_results)
    validate_negative_layoff_values(raw_df, validation_results)
    validate_percentage_range(raw_df, validation_results)
    validate_date_column(raw_df, validation_results)
    validate_cleaned_file_exists(validation_results)
    validate_visual_files_exist(validation_results)

    validation_report = generate_validation_report(validation_results)
    save_report(validation_report, REPORT_FILE_PATH)