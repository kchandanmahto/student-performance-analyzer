from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "students.csv"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
CLEANED_DATA_PATH = PROCESSED_DIR / "cleaned_students.csv"

REQUIRED_COLUMNS = [
    "student_id",
    "student_name",
    "attendance_percentage",
    "study_hours_per_day",
    "previous_marks",
    "assignment_score",
    "final_marks",
]

NUMERIC_COLUMNS = [
    "attendance_percentage",
    "study_hours_per_day",
    "previous_marks",
    "assignment_score",
    "final_marks",
]


def load_raw_data(file_path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Load the original student dataset."""

    if not file_path.exists():
        raise FileNotFoundError(
            f"Raw dataset not found: {file_path}. "
            "Run the data collection phase first."
        )

    return pd.read_csv(file_path)


def validate_columns(df: pd.DataFrame) -> None:
    """Check whether all required columns are available."""

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Dataset is missing required columns: {missing_columns}"
        )


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean missing values, duplicates and invalid records."""

    validate_columns(df)

    cleaned = df.copy()

    # Remove duplicate records.
    cleaned = cleaned.drop_duplicates()

    # Convert numeric columns to numeric values.
    for column in NUMERIC_COLUMNS:
        cleaned[column] = pd.to_numeric(
            cleaned[column], errors="coerce"
        )

    # Replace invalid values with missing values.
    valid_ranges = {
        "attendance_percentage": (0, 100),
        "study_hours_per_day": (0, 24),
        "previous_marks": (0, 100),
        "assignment_score": (0, 100),
        "final_marks": (0, 100),
    }

    for column, (minimum, maximum) in valid_ranges.items():
        invalid = (
            (cleaned[column] < minimum)
            | (cleaned[column] > maximum)
        )
        cleaned.loc[invalid, column] = float("nan")

    # Fill missing numerical values using the median.
    for column in NUMERIC_COLUMNS:
        median_value = cleaned[column].median()

        if pd.isna(median_value):
            raise ValueError(
                f"Cannot clean {column}: all values are missing."
            )

        cleaned[column] = cleaned[column].fillna(median_value)

    # Remove records without essential student identity.
    cleaned["student_id"] = cleaned["student_id"].astype("string").str.strip()
    cleaned["student_name"] = cleaned["student_name"].astype("string").str.strip()

    cleaned = cleaned.dropna(
        subset=["student_id", "student_name"]
    )

    cleaned = cleaned[
        (cleaned["student_id"] != "")
        & (cleaned["student_name"] != "")
    ]

    # Ensure each student ID is unique.
    cleaned = cleaned.drop_duplicates(
        subset=["student_id"], keep="first"
    )

    return cleaned.reset_index(drop=True)


def save_cleaned_data(df: pd.DataFrame) -> Path:
    """Save cleaned data to the processed directory."""

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEANED_DATA_PATH, index=False)

    return CLEANED_DATA_PATH


def run_cleaning() -> pd.DataFrame:
    """Execute the complete data cleaning workflow."""

    print("\n" + "=" * 50)
    print("DATA CLEANING")
    print("=" * 50)

    raw_df = load_raw_data()

    print(f"Original rows: {len(raw_df)}")
    print(f"Original columns: {len(raw_df.columns)}")
    print(f"Missing values before cleaning: {raw_df.isna().sum().sum()}")
    print(f"Duplicate rows before cleaning: {raw_df.duplicated().sum()}")

    cleaned_df = clean_data(raw_df)
    output_path = save_cleaned_data(cleaned_df)

    print("\nCleaning completed successfully.")
    print(f"Rows after cleaning: {len(cleaned_df)}")
    print(f"Missing values after cleaning: {cleaned_df.isna().sum().sum()}")
    print(f"Duplicate rows after cleaning: {cleaned_df.duplicated().sum()}")
    print(f"Unique student IDs: {cleaned_df['student_id'].nunique()}")
    print(f"Saved file: {output_path}")

    return cleaned_df


if __name__ == "__main__":
    run_cleaning()
