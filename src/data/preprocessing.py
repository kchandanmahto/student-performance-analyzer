from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler


PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_PATH = PROJECT_ROOT / "data" / "processed" / "engineered_students.csv"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
MODEL_DIR = PROJECT_ROOT / "models"

TRAIN_PATH = PROCESSED_DIR / "train_data.csv"
TEST_PATH = PROCESSED_DIR / "test_data.csv"
PREPROCESSOR_PATH = MODEL_DIR / "preprocessor.joblib"


NUMERIC_FEATURES = [
    "attendance_percentage",
    "study_hours_per_day",
    "previous_marks",
    "assignment_score",
    "internal_average",
    "academic_engagement_score",
]

CATEGORICAL_FEATURES = [
    "attendance_category",
    "study_category",
    "previous_performance",
]

TARGET = "final_marks"


def load_data():
    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            "Engineered dataset not found. Run feature engineering first."
        )

    return pd.read_csv(INPUT_PATH)


def transform_data(df):
    required_columns = (
        NUMERIC_FEATURES + CATEGORICAL_FEATURES + [TARGET]
    )

    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if df[required_columns].isnull().any().any():
        raise ValueError("Missing values found. Clean the dataset first.")

    X = df[NUMERIC_FEATURES + CATEGORICAL_FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), NUMERIC_FEATURES),
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                CATEGORICAL_FEATURES
            ),
        ]
    )

    # Fit only on training data to prevent data leakage.
    X_train_transformed = preprocessor.fit_transform(X_train)
    X_test_transformed = preprocessor.transform(X_test)

    feature_names = preprocessor.get_feature_names_out()

    X_train_df = pd.DataFrame(
        X_train_transformed,
        columns=feature_names,
        index=X_train.index
    )

    X_test_df = pd.DataFrame(
        X_test_transformed,
        columns=feature_names,
        index=X_test.index
    )

    train_data = X_train_df.copy()
    train_data[TARGET] = y_train

    test_data = X_test_df.copy()
    test_data[TARGET] = y_test

    return train_data, test_data, preprocessor


def save_outputs(train_data, test_data, preprocessor):
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    train_data.to_csv(TRAIN_PATH, index=False)
    test_data.to_csv(TEST_PATH, index=False)

    joblib.dump(preprocessor, PREPROCESSOR_PATH)

    print("\nFiles saved successfully:")
    print(TRAIN_PATH)
    print(TEST_PATH)
    print(PREPROCESSOR_PATH)


def run_preprocessing():
    print("\n========== DATA TRANSFORMATION ==========")

    df = load_data()

    print("Original Dataset Shape:", df.shape)

    train_data, test_data, preprocessor = transform_data(df)

    save_outputs(train_data, test_data, preprocessor)

    print("\nTraining Dataset Shape:", train_data.shape)
    print("Testing Dataset Shape:", test_data.shape)
    print(
        "Training Percentage:",
        f"{len(train_data) / len(df) * 100:.1f}%"
    )
    print(
        "Testing Percentage:",
        f"{len(test_data) / len(df) * 100:.1f}%"
    )

    print("\nTransformed Features:")
    print(preprocessor.get_feature_names_out().tolist())

    print("\nData Transformation completed successfully!")


if __name__ == "__main__":
    run_preprocessing()
