from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = PROJECT_ROOT / "data" / "processed" / "cleaned_students.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "engineered_students.csv"


def load_data():
    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            f"Cleaned dataset not found: {INPUT_PATH}"
        )

    return pd.read_csv(INPUT_PATH)


def engineer_features(df):
    df = df.copy()

    required_columns = [
        "attendance_percentage",
        "study_hours_per_day",
        "previous_marks",
        "assignment_score",
        "final_marks",
    ]

    missing_columns = [
        col for col in required_columns if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    # Feature 1: Average of previous marks and assignment score
    df["internal_average"] = (
        df["previous_marks"] + df["assignment_score"]
    ) / 2

    # Feature 2: Attendance category
    df["attendance_category"] = pd.cut(
        df["attendance_percentage"],
        bins=[-1, 60, 75, 100],
        labels=["Low", "Medium", "High"]
    )

    # Feature 3: Study category
    df["study_category"] = pd.cut(
        df["study_hours_per_day"],
        bins=[-1, 2, 5, 24],
        labels=["Low", "Medium", "High"]
    )

    # Feature 4: Academic engagement score
    df["academic_engagement_score"] = (
        0.5 * df["attendance_percentage"]
        + 0.5 * (df["study_hours_per_day"] / 24 * 100)
    )

    # Feature 5: Previous academic performance category
    df["previous_performance"] = pd.cut(
        df["previous_marks"],
        bins=[-1, 40, 60, 75, 100],
        labels=["Poor", "Average", "Good", "Excellent"]
    )

    return df


def save_engineered_data(df):
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"\nEngineered dataset saved: {OUTPUT_PATH}")


def run_feature_engineering():
    print("\n========== FEATURE ENGINEERING ==========")

    df = load_data()

    print("\nOriginal Shape:", df.shape)

    engineered_df = engineer_features(df)

    print("\nNew Shape:", engineered_df.shape)

    print("\nNew Features:")
    new_features = [
        "internal_average",
        "attendance_category",
        "study_category",
        "academic_engagement_score",
        "previous_performance",
    ]

    print(engineered_df[new_features].head(10).to_string(index=False))

    save_engineered_data(engineered_df)

    print("\nFeature Engineering completed successfully!")


if __name__ == "__main__":
    run_feature_engineering()
