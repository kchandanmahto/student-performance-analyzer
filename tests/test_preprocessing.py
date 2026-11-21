from pathlib import Path

import pandas as pd

from src.data.preprocessing import transform_data


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "engineered_students.csv"


def test_preprocessing_creates_train_test_data():
    df = pd.read_csv(DATA_PATH)

    train_data, test_data, preprocessor = transform_data(df)

    assert len(train_data) == 400
    assert len(test_data) == 100

    assert "final_marks" in train_data.columns
    assert "final_marks" in test_data.columns

    assert train_data.isnull().sum().sum() == 0
    assert test_data.isnull().sum().sum() == 0

    assert len(preprocessor.get_feature_names_out()) == 16
