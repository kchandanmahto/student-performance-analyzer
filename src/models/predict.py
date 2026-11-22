from pathlib import Path

import joblib
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_DIR = PROJECT_ROOT / "models"
PREPROCESSOR_PATH = MODEL_DIR / "preprocessor.joblib"

MODEL_FILES = {
    "1": ("Linear Regression", "linear_regression.joblib"),
    "2": ("Random Forest", "random_forest.joblib"),
}


def create_student_features(
    attendance,
    study_hours,
    previous_marks,
    assignment_score
):
    if not 0 <= attendance <= 100:
        raise ValueError("Attendance must be between 0 and 100.")

    if not 0 <= study_hours <= 24:
        raise ValueError("Study hours must be between 0 and 24.")

    if not 0 <= previous_marks <= 100:
        raise ValueError("Previous marks must be between 0 and 100.")

    if not 0 <= assignment_score <= 100:
        raise ValueError("Assignment score must be between 0 and 100.")

    internal_average = (previous_marks + assignment_score) / 2

    academic_engagement_score = (
        0.5 * attendance
        + 0.5 * (study_hours / 24 * 100)
    )

    attendance_category = pd.cut(
        pd.Series([attendance]),
        bins=[-1, 60, 75, 100],
        labels=["Low", "Medium", "High"]
    ).iloc[0]

    study_category = pd.cut(
        pd.Series([study_hours]),
        bins=[-1, 2, 5, 24],
        labels=["Low", "Medium", "High"]
    ).iloc[0]

    previous_performance = pd.cut(
        pd.Series([previous_marks]),
        bins=[-1, 40, 60, 75, 100],
        labels=["Poor", "Average", "Good", "Excellent"]
    ).iloc[0]

    return pd.DataFrame([{
        "attendance_percentage": attendance,
        "study_hours_per_day": study_hours,
        "previous_marks": previous_marks,
        "assignment_score": assignment_score,
        "internal_average": internal_average,
        "academic_engagement_score": academic_engagement_score,
        "attendance_category": attendance_category,
        "study_category": study_category,
        "previous_performance": previous_performance,
    }])


def predict_student_performance(
    attendance,
    study_hours,
    previous_marks,
    assignment_score,
    model_choice="2"
):
    if model_choice not in MODEL_FILES:
        raise ValueError("Invalid model choice. Select 1 or 2.")

    model_name, model_filename = MODEL_FILES[model_choice]
    model_path = MODEL_DIR / model_filename

    if not PREPROCESSOR_PATH.exists():
        raise FileNotFoundError("Preprocessor not found. Run preprocessing first.")

    if not model_path.exists():
        raise FileNotFoundError(
            f"{model_filename} not found. Run model training first."
        )

    student_data = create_student_features(
        attendance,
        study_hours,
        previous_marks,
        assignment_score
    )

    preprocessor = joblib.load(PREPROCESSOR_PATH)
    model = joblib.load(model_path)

    transformed_data = preprocessor.transform(student_data)

    transformed_df = pd.DataFrame(
        transformed_data,
        columns=preprocessor.get_feature_names_out()
    )

    prediction = model.predict(transformed_df)[0]
    prediction = max(0, min(100, float(prediction)))

    return {
        "model": model_name,
        "predicted_marks": round(prediction, 2),
    }


def run_prediction():
    print("\n========== STUDENT PERFORMANCE PREDICTION ==========")

    try:
        print("\nEnter Student Details:")

        attendance = float(input("Attendance percentage (0-100): "))
        study_hours = float(input("Study hours per day (0-24): "))
        previous_marks = float(input("Previous marks (0-100): "))
        assignment_score = float(input("Assignment score (0-100): "))

        print("\nSelect Machine Learning Model:")
        print("1. Linear Regression")
        print("2. Random Forest")

        model_choice = input("Enter choice (1 or 2): ").strip()

        result = predict_student_performance(
            attendance,
            study_hours,
            previous_marks,
            assignment_score,
            model_choice
        )

        print("\n========== PREDICTION RESULT ==========")
        print("Selected Model:", result["model"])
        print("Predicted Final Marks:", result["predicted_marks"], "/ 100")

    except ValueError as error:
        print("\nInvalid input:", error)

    except FileNotFoundError as error:
        print("\nRequired file missing:", error)


if __name__ == "__main__":
    run_prediction()
