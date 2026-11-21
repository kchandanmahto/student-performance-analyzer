from pathlib import Path

import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
DATASET_PATH = RAW_DATA_DIR / "students.csv"


def generate_synthetic_dataset(
    n_students: int = 500,
    random_state: int = 42,
    include_data_issues: bool = True,
) -> pd.DataFrame:
    """Generate synthetic student performance data for practice."""

    if n_students < 10:
        raise ValueError("n_students must be at least 10.")

    rng = np.random.default_rng(random_state)

    attendance = rng.uniform(45, 100, n_students)
    study_hours = rng.uniform(0.5, 10, n_students)
    previous_marks = rng.uniform(30, 100, n_students)
    assignment_score = rng.uniform(35, 100, n_students)

    noise = rng.normal(0, 5, n_students)

    final_marks = (
        0.25 * attendance
        + 3.0 * study_hours
        + 0.35 * previous_marks
        + 0.20 * assignment_score
        + noise
    )

    final_marks = np.clip(final_marks, 0, 100)

    data = {
        "student_id": [
            f"STU{i:04d}" for i in range(1, n_students + 1)
        ],
        "student_name": [
            f"Student_{i:04d}" for i in range(1, n_students + 1)
        ],
        "attendance_percentage": np.round(attendance, 2),
        "study_hours_per_day": np.round(study_hours, 2),
        "previous_marks": np.round(previous_marks, 2),
        "assignment_score": np.round(assignment_score, 2),
        "final_marks": np.round(final_marks, 2),
    }

    df = pd.DataFrame(data)

    if include_data_issues:
        # Add missing values for the upcoming cleaning phase.
        missing_rows = rng.choice(
            df.index, size=max(1, n_students // 50), replace=False
        )
        df.loc[missing_rows, "attendance_percentage"] = np.nan

        missing_rows = rng.choice(
            df.index, size=max(1, n_students // 50), replace=False
        )
        df.loc[missing_rows, "assignment_score"] = np.nan

        # Add a few duplicate records intentionally.
        duplicate_count = min(5, n_students)
        duplicates = df.sample(
            n=duplicate_count, random_state=random_state
        )
        df = pd.concat([df, duplicates], ignore_index=True)

    return df


def collect_data(
    n_students: int = 500,
    random_state: int = 42,
    include_data_issues: bool = True,
) -> Path:
    """Generate the dataset and save it as a CSV file."""

    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    df = generate_synthetic_dataset(
        n_students=n_students,
        random_state=random_state,
        include_data_issues=include_data_issues,
    )

    df.to_csv(DATASET_PATH, index=False)

    print("Data collection completed successfully.")
    print(f"Dataset location: {DATASET_PATH}")
    print(f"Total rows: {len(df)}")
    print(f"Total columns: {len(df.columns)}")
    print(f"Missing values: {int(df.isna().sum().sum())}")
    print(f"Duplicate rows: {int(df.duplicated().sum())}")

    return DATASET_PATH


def load_dataset(file_path: Path = DATASET_PATH) -> pd.DataFrame:
    """Load a CSV dataset into a Pandas DataFrame."""

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}. Run data collection first."
        )

    return pd.read_csv(file_path)


if __name__ == "__main__":
    collect_data()
