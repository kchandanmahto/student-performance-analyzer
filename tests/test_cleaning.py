import pandas as pd

from src.data.cleaning import clean_data


def test_clean_data_removes_duplicates_and_fills_missing_values():
    data = pd.DataFrame({
        "student_id": ["S001", "S002", "S001"],
        "student_name": ["Aman", "Rahul", "Aman"],
        "attendance_percentage": [85, None, 85],
        "study_hours_per_day": [4, 3, 4],
        "previous_marks": [70, 65, 70],
        "assignment_score": [80, 75, 80],
        "final_marks": [82, 70, 82],
    })

    cleaned = clean_data(data)

    assert len(cleaned) == 2
    assert cleaned.isnull().sum().sum() == 0
    assert cleaned["student_id"].duplicated().sum() == 0
