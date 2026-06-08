# US Tech Layoffs Data Analysis & Data Quality Validation

This project analyzes US tech layoffs data using Python, Pandas, Matplotlib, and Seaborn.
It focuses not only on exploratory data analysis, but also on data quality validation and data cleaning before generating insights.

The goal of this project is to demonstrate how raw business data can be validated, cleaned, analyzed, visualized, and summarized in a professional data analysis workflow.

## Project Objective

The objective of this project is to analyze layoffs trends across companies, industries, locations, and time periods while applying data quality checks to ensure the insights are reliable.

## Dataset

The dataset contains technology layoff records with fields such as:

* Company
* Location
* Industry
* Total laid off
* Percentage laid off
* Date
* Company stage
* Country
* Funds raised

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* GitHub
* IntelliJ IDEA / Terminal

## Project Structure

```text
us-tech-layoffs-data-analysis
├── data
│   ├── raw
│   │   └── layoffs.csv
│   └── cleaned
│       └── cleaned_layoffs.csv
├── reports
│   └── layoffs_summary_report.txt
├── src
│   ├── data_quality_checks.py
│   ├── data_cleaning.py
│   ├── exploratory_analysis.py
│   └── generate_summary_report.py
├── visuals
│   ├── top_companies_by_layoffs.png
│   ├── top_industries_by_layoffs.png
│   ├── layoffs_trend_by_year.png
│   └── top_locations_by_layoffs.png
├── requirements.txt
├── .gitignore
└── README.md
```

## Data Quality Checks

The project includes data quality validation before analysis. The checks include:

* Dataset shape validation
* Column validation
* Missing value analysis
* Duplicate record detection
* Negative layoff count validation
* Invalid percentage validation
* Invalid or missing date validation

## Data Cleaning Steps

The cleaning script performs the following steps:

* Removes duplicate records
* Standardizes text columns
* Converts date values into proper datetime format
* Converts numeric fields into valid numeric data types
* Creates year, month, and year-month columns for trend analysis
* Saves the cleaned dataset into `data/cleaned/cleaned_layoffs.csv`

## Exploratory Data Analysis

The analysis focuses on:

* Top companies by total layoffs
* Top industries impacted by layoffs
* Layoff trends by year
* Top locations by layoffs
* Business-level summary insights

## Key Insights

Based on the cleaned dataset:

* Total layoffs recorded: 383,659
* Total unique companies: 1,890
* Total industries impacted: 32
* Date range analyzed: 2020-03-11 to 2023-03-06
* Top companies by layoffs include Amazon, Google, Meta, Salesforce, and Microsoft
* Top impacted industries include Consumer, Retail, Other, Transportation, and Finance

## Visualizations

The project generates visual charts and saves them in the `visuals` folder:

* Top 10 Companies by Total Layoffs
* Top 10 Industries by Total Layoffs
* Layoffs Trend by Year
* Top 10 Locations by Total Layoffs

## Summary Report

A business summary report is generated and saved at:

```text
reports/layoffs_summary_report.txt
```

The report includes:

* Overall dataset summary
* Top companies by layoffs
* Top industries by layoffs
* Top locations by layoffs
* Business observations

## How to Run the Project

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

Run exploratory analysis and generate visuals:

```bash
python3 src/exploratory_analysis.py
```

Generate summary report:

```bash
python3 src/generate_summary_report.py
```

## What I Practiced

Through this project, I practiced:

* Loading and analyzing CSV data using Pandas
* Performing data quality checks before analysis
* Cleaning and transforming raw data
* Handling missing values, duplicates, invalid dates, and numeric conversions
* Creating reusable Python scripts for different stages of the workflow
* Generating visual charts using Matplotlib and Seaborn
* Creating a business summary report from cleaned data
* Organizing a data analysis project in a GitHub-friendly structure

## Future Enhancements

Planned improvements for this project:

* Add notebook-based analysis
* Add more advanced visualizations
* Add location-wise and industry-wise trend analysis
* Add automated data validation report
* Add Power BI or Tableau dashboard
* Add unit tests for data quality checks

## Author

Mahigna Reddy
