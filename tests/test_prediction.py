import pytest

from src.models.predict import (
    create_student_features,
    predict_student_performance,
)


def test_feature_creation():
    df = create_student_features(85, 5, 75, 80)

    assert len(df) == 1
    assert "internal_average" in df.columns
    assert "academic_engagement_score" in df.columns
    assert df.iloc[0]["internal_average"] == 77.5


@pytest.mark.parametrize(
    "attendance,study,previous,assignment",
    [
        (-1, 5, 75, 80),
        (101, 5, 75, 80),
        (85, -1, 75, 80),
        (85, 25, 75, 80),
        (85, 5, 101, 80),
        (85, 5, 75, -1),
    ],
)
def test_invalid_student_inputs(attendance, study, previous, assignment):
    with pytest.raises(ValueError):
        create_student_features(
            attendance,
            study,
            previous,
            assignment
        )


def test_invalid_model_choice():
    with pytest.raises(ValueError):
        predict_student_performance(85, 5, 75, 80, "3")


def test_random_forest_prediction():
    result = predict_student_performance(85, 5, 75, 80, "2")

    assert result["model"] == "Random Forest"
    assert isinstance(result["predicted_marks"], float)
    assert 0 <= result["predicted_marks"] <= 100


def test_linear_regression_prediction():
    result = predict_student_performance(85, 5, 75, 80, "1")

    assert result["model"] == "Linear Regression"
    assert 0 <= result["predicted_marks"] <= 100
