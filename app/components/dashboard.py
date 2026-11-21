from pathlib import Path

import pandas as pd
import streamlit as st

from src.models.predict import predict_student_performance


PROJECT_ROOT = Path(__file__).resolve().parents[2]
EVALUATION_PATH = PROJECT_ROOT / "reports" / "model_evaluation.csv"
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "cleaned_students.csv"


def show_overview():
    st.subheader("Project Overview")

    if DATA_PATH.exists():
        df = pd.read_csv(DATA_PATH)

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Students", len(df))
        col2.metric("Average Marks", f"{df['final_marks'].mean():.2f}")
        col3.metric("Average Attendance", f"{df['attendance_percentage'].mean():.1f}%")
    else:
        st.info("Cleaned dataset is not available.")


def show_model_comparison():
    st.subheader("Model Performance Comparison")

    if not EVALUATION_PATH.exists():
        st.info("Evaluation report not found. Run model evaluation first.")
        return

    results = pd.read_csv(EVALUATION_PATH)

    st.dataframe(
        results.round(4),
        use_container_width=True,
        hide_index=True
    )

    if "Model" in results.columns and "MAE" in results.columns:
        st.caption("Lower MAE indicates a smaller average prediction error.")
        st.bar_chart(results.set_index("Model")[["MAE", "RMSE"]])


def show_prediction():
    st.subheader("Predict Student Performance")

    st.write("Enter student academic details to estimate final marks.")

    with st.form("prediction_form"):
        col1, col2 = st.columns(2)

        with col1:
            attendance = st.number_input(
                "Attendance (%)",
                min_value=0.0,
                max_value=100.0,
                value=85.0,
                step=1.0
            )

            study_hours = st.number_input(
                "Study Hours Per Day",
                min_value=0.0,
                max_value=24.0,
                value=5.0,
                step=0.5
            )

        with col2:
            previous_marks = st.number_input(
                "Previous Marks",
                min_value=0.0,
                max_value=100.0,
                value=75.0,
                step=1.0
            )

            assignment_score = st.number_input(
                "Assignment Score",
                min_value=0.0,
                max_value=100.0,
                value=80.0,
                step=1.0
            )

        model_name = st.selectbox(
            "Select Machine Learning Model",
            ["Random Forest", "Linear Regression"]
        )

        submitted = st.form_submit_button(
            "Predict Final Marks",
            use_container_width=True
        )

    if submitted:
        model_choice = "2" if model_name == "Random Forest" else "1"

        try:
            result = predict_student_performance(
                attendance,
                study_hours,
                previous_marks,
                assignment_score,
                model_choice
            )

            st.success("Prediction completed successfully!")

            col1, col2 = st.columns(2)

            col1.metric(
                "Predicted Final Marks",
                f"{result['predicted_marks']} / 100"
            )

            col2.metric("Selected Model", result["model"])

            st.progress(
                int(round(result["predicted_marks"]))
            )

            st.caption(
                "This is an estimate based on synthetic training data, "
                "not a guarantee of actual exam performance."
            )

        except (ValueError, FileNotFoundError) as error:
            st.error(str(error))


def render_dashboard():
    st.title("Student Performance Analyzer")
    st.write(
        "Analyze student data and predict academic performance "
        "using Machine Learning."
    )

    st.divider()

    show_overview()

    st.divider()

    show_prediction()

    st.divider()

    show_model_comparison()

    st.divider()

    st.caption("Student Performance Analyzer | Data Science Project")
