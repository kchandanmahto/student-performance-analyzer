from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "cleaned_students.csv"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"
REPORT_PATH = PROJECT_ROOT / "reports" / "analysis_report.md"

FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def load_data():
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Cleaned dataset not found: {DATA_PATH}. Run data cleaning first."
        )

    return pd.read_csv(DATA_PATH)


def generate_summary(df):
    numeric_df = df.select_dtypes(include="number")

    summary = numeric_df.describe().round(2)
    correlation = numeric_df.corr().round(2)

    return summary, correlation


def create_visualizations(df):
    sns.set_theme(style="whitegrid")

    # 1. Final marks distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(df["final_marks"], bins=20, kde=True)
    plt.title("Distribution of Final Marks")
    plt.xlabel("Final Marks")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "marks_distribution.png")
    plt.close()

    # 2. Study hours vs final marks
    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x="study_hours_per_day",
        y="final_marks"
    )
    plt.title("Study Hours vs Final Marks")
    plt.xlabel("Study Hours Per Day")
    plt.ylabel("Final Marks")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "study_hours_vs_marks.png")
    plt.close()

    # 3. Attendance vs final marks
    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x="attendance_percentage",
        y="final_marks"
    )
    plt.title("Attendance vs Final Marks")
    plt.xlabel("Attendance Percentage")
    plt.ylabel("Final Marks")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "attendance_vs_marks.png")
    plt.close()

    # 4. Correlation heatmap
    numeric_df = df.select_dtypes(include="number")
    plt.figure(figsize=(9, 6))
    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "correlation_heatmap.png")
    plt.close()

    print("All visualizations saved successfully.")


def generate_report(df, summary, correlation):
    report = f"""# Student Performance Analysis Report

## Dataset Overview

- Total students: {len(df)}
- Total columns: {len(df.columns)}
- Missing values: {df.isnull().sum().sum()}

## Statistical Summary

{summary.to_markdown()}

## Correlation Analysis

{correlation.to_markdown()}

## Key Observations

- Average final marks: {df['final_marks'].mean():.2f}
- Highest final marks: {df['final_marks'].max():.2f}
- Lowest final marks: {df['final_marks'].min():.2f}
- Average attendance: {df['attendance_percentage'].mean():.2f}%
- Average study hours: {df['study_hours_per_day'].mean():.2f} hours/day

## Visualizations

See the `reports/figures/` folder for generated charts.
"""

    REPORT_PATH.write_text(report, encoding="utf-8")
    print(f"Analysis report saved: {REPORT_PATH}")


def run_eda():
    print("\n========== EXPLORATORY DATA ANALYSIS ==========")

    df = load_data()

    print("\nDataset Shape:", df.shape)
    print("\nFirst 5 Rows:")
    print(df.head().to_string(index=False))

    summary, correlation = generate_summary(df)

    print("\nStatistical Summary:")
    print(summary)

    print("\nCorrelation Matrix:")
    print(correlation)

    create_visualizations(df)
    generate_report(df, summary, correlation)

    print("\nEDA completed successfully!")


if __name__ == "__main__":
    run_eda()
