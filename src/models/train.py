from pathlib import Path

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression


PROJECT_ROOT = Path(__file__).resolve().parents[2]

TRAIN_PATH = PROJECT_ROOT / "data" / "processed" / "train_data.csv"
MODEL_DIR = PROJECT_ROOT / "models"

TARGET = "final_marks"


def load_training_data():
    if not TRAIN_PATH.exists():
        raise FileNotFoundError(
            "Training data not found. Run preprocessing first."
        )

    df = pd.read_csv(TRAIN_PATH)

    if TARGET not in df.columns:
        raise ValueError(f"Target column '{TARGET}' not found.")

    if df.isnull().any().any():
        raise ValueError("Training dataset contains missing values.")

    X = df.drop(columns=[TARGET])
    y = df[TARGET]

    return X, y


def train_models(X, y):
    models = {
        "Linear Regression": LinearRegression(),

        "Random Forest": RandomForestRegressor(
            n_estimators=200,
            max_depth=10,
            min_samples_split=4,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1
        )
    }

    trained_models = {}

    for name, model in models.items():
        print(f"\nTraining {name}...")

        model.fit(X, y)

        trained_models[name] = model

        print(f"{name} training completed!")

    return trained_models


def save_models(trained_models):
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    model_files = {
        "Linear Regression": "linear_regression.joblib",
        "Random Forest": "random_forest.joblib"
    }

    for name, model in trained_models.items():
        model_path = MODEL_DIR / model_files[name]

        joblib.dump(model, model_path)

        print(f"Saved: {model_path}")


def run_training():
    print("\n========== MODEL TRAINING ==========")

    X, y = load_training_data()

    print("\nTraining Features:", X.shape)
    print("Target Shape:", y.shape)

    trained_models = train_models(X, y)

    save_models(trained_models)

    print("\nAll models trained and saved successfully!")


if __name__ == "__main__":
    run_training()
