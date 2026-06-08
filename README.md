# US Tech Layoffs Data Analysis & Data Quality Validation

This project analyzes tech layoffs data using Python and focuses on both **data analysis** and **data quality validation**.

The goal is to show how raw data can be validated, cleaned, analyzed, visualized, and summarized before generating business insights.

## Project Objective

* Validate raw layoffs data for quality issues
* Clean and prepare the dataset for analysis
* Analyze layoffs by company, industry, location, and time period
* Generate visual charts and summary reports
* Create an automated validation report with PASS, WARNING, and FAIL results

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* GitHub
* Terminal / IntelliJ IDEA

## Project Structure

```text
us-tech-layoffs-data-analysis
├── data
│   ├── raw
│   └── cleaned
├── reports
│   ├── layoffs_summary_report.txt
│   └── data_validation_report.txt
├── src
│   ├── data_quality_checks.py
│   ├── data_cleaning.py
│   ├── exploratory_analysis.py
│   ├── trend_analysis.py
│   ├── generate_summary_report.py
│   └── generate_data_validation_report.py
├── visuals
├── requirements.txt
├── .gitignore
└── README.md
```

## What This Project Does

### Data Quality Checks

The project validates:

* Required columns
* Missing values
* Duplicate records
* Invalid dates
* Negative layoff values
* Invalid percentage values
* Cleaned file generation
* Visual file generation

### Data Cleaning

The cleaning script:

* Removes duplicate records
* Standardizes text columns
* Converts date and numeric fields
* Creates year, month, and year-month columns
* Saves the cleaned dataset

### Analysis and Visualizations

The project analyzes:

* Top companies by layoffs
* Top industries impacted
* Top locations impacted
* Layoffs trend by year
* Monthly layoffs trend
* Industry-wise and location-wise trends

Charts are saved in the `visuals` folder.

### Reports Generated

The project generates:

* `layoffs_summary_report.txt`
* `data_validation_report.txt`

The data validation report shows:

* Total checks executed: 8
* Passed checks: 5
* Warnings: 3
* Failed checks: 0

## Key Insights

From the cleaned dataset:

* Total layoffs recorded: 383,659
* Unique companies analyzed: 1,890
* Industries impacted: 32
* Date range: 2020-03-11 to 2023-03-06
* Top companies include Amazon, Google, Meta, Salesforce, and Microsoft
* Top industries include Consumer, Retail, Other, Transportation, and Finance

## How to Run

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run data quality checks:

```bash
python3 src/data_quality_checks.py
```

Run data cleaning:

```bash
python3 src/data_cleaning.py
```

Run exploratory analysis:

```bash
python3 src/exploratory_analysis.py
```

Run trend analysis:

```bash
python3 src/trend_analysis.py
```

Generate summary report:

```bash
python3 src/generate_summary_report.py
```

Generate data validation report:

```bash
python3 src/generate_data_validation_report.py
```

## Why This Project Matters

In real-world analysis, raw data should not be used directly without validation. This project demonstrates a structured workflow where data is first validated, cleaned, analyzed, visualized, and then summarized.

It is useful for QA, SDET, Data QA, and data-focused candidates who want to understand how data quality and analysis work together.

## Future Enhancements

* Add notebook-based analysis
* Add Power BI or Tableau dashboard
* Add unit tests for data quality checks
* Add SQL-based analysis
* Add GitHub Actions workflow

## Author

Mahigna Reddy
