from pathlib import Path

import joblib
import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]

TEST_PATH = PROJECT_ROOT / "data" / "processed" / "test_data.csv"
MODEL_DIR = PROJECT_ROOT / "models"
REPORT_DIR = PROJECT_ROOT / "reports"

TARGET = "final_marks"

MODEL_FILES = {
    "Linear Regression": "linear_regression.joblib",
    "Random Forest": "random_forest.joblib",
}


def load_test_data():
    if not TEST_PATH.exists():
        raise FileNotFoundError("Test dataset not found. Run preprocessing first.")

    df = pd.read_csv(TEST_PATH)

    if TARGET not in df.columns:
        raise ValueError(f"Target column '{TARGET}' not found.")

    X_test = df.drop(columns=[TARGET])
    y_test = df[TARGET]

    return X_test, y_test


def evaluate_models(X_test, y_test):
    results = []

    for model_name, filename in MODEL_FILES.items():
        model_path = MODEL_DIR / filename

        if not model_path.exists():
            raise FileNotFoundError(
                f"{filename} not found. Run model training first."
            )

        model = joblib.load(model_path)

        predictions = model.predict(X_test)

        mse = mean_squared_error(y_test, predictions)

        metrics = {
            "Model": model_name,
            "MAE": mean_absolute_error(y_test, predictions),
            "MSE": mse,
            "RMSE": mse ** 0.5,
            "R2 Score": r2_score(y_test, predictions),
        }

        results.append(metrics)

    return pd.DataFrame(results)


def save_results(results):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    output_path = REPORT_DIR / "model_evaluation.csv"
    results.to_csv(output_path, index=False)

    print(f"\nEvaluation results saved: {output_path}")


def run_evaluation():
    print("\n========== MODEL EVALUATION ==========")

    X_test, y_test = load_test_data()

    print("Testing Records:", len(X_test))

    results = evaluate_models(X_test, y_test)

    print("\nModel Performance:")
    print(results.round(4).to_string(index=False))

    best_model = results.loc[results["MAE"].idxmin(), "Model"]

    print("\nBest Model based on MAE:", best_model)

    save_results(results)

    print("\nModel evaluation completed successfully!")


if __name__ == "__main__":
    run_evaluation()
