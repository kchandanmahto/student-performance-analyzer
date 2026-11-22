
# StudentIQ – Machine Learning Documentation

## 1. Overview

StudentIQ uses supervised machine learning to estimate student final marks from selected academic features.

The project currently implements two regression algorithms:

- Linear Regression
- Random Forest Regressor

The machine learning workflow includes data preparation, preprocessing, model training, evaluation, and prediction.

## 2. Machine Learning Workflow

```text
Student Academic Dataset
          |
          v
    Data Preparation
          |
          v
   Feature Engineering
          |
          v
    Data Preprocessing
          |
          v
      Train / Test
          |
          v
     Model Training
          |
          v
    Model Evaluation
          |
          v
   Saved Model Artifacts
          |
          v
    Prediction Engine
          |
          v
    Estimated Marks
```

## 3. Input Features

The prediction workflow uses the following academic attributes:

| Feature | Description |
|---|---|
| attendance_percentage | Student attendance percentage |
| study_hours_per_day | Average daily study hours |
| previous_marks | Previous academic marks |
| assignment_score | Assignment performance score |

Additional engineered features include:

- internal_average
- attendance_category
- study_category
- academic_engagement_score
- previous_performance

The target variable is `final_marks`.

## 4. Data Preprocessing

The project uses a saved preprocessing pipeline to prepare model inputs.

Preprocessing includes:

- Numerical feature transformation.
- Categorical feature encoding.
- Consistent feature preparation.
- Reusing the same fitted preprocessor during prediction.

The saved preprocessing artifact is:

`models/preprocessor.joblib`

The transformed feature names are obtained from the fitted preprocessor to maintain consistency between training and prediction.

## 5. Machine Learning Algorithms

### 5.1 Linear Regression

Linear Regression is a supervised learning algorithm used to estimate a continuous numerical target.

In StudentIQ, it serves as a regression model for estimating student final marks.

### 5.2 Random Forest Regressor

Random Forest Regressor is an ensemble learning algorithm based on multiple decision trees.

It combines predictions from multiple trees to produce a regression estimate.

StudentIQ uses this algorithm as another model for student marks prediction.

## 6. Model Training

The training module is:

`src/models/train.py`

The training workflow uses prepared training data and fits the selected regression algorithms.

The project stores trained model artifacts in the `models/` directory.

Current model artifacts:

| File | Purpose |
|---|---|
| linear_regression.joblib | Saved Linear Regression model |
| random_forest.joblib | Saved Random Forest model |
| preprocessor.joblib | Saved preprocessing pipeline |

## 7. Model Evaluation

The evaluation module is:

`src/models/evaluate.py`

The project uses the following regression metrics.

### Mean Absolute Error (MAE)

Measures the average absolute difference between actual and predicted values.

### Mean Squared Error (MSE)

Measures the average squared difference between actual and predicted values.

### Root Mean Squared Error (RMSE)

Measures prediction error using the square root of MSE.

### R² Score

Measures how much of the variation in the target variable is explained by the regression model.

## 8. Prediction Workflow

The prediction module is:

`src/models/predict.py`

The prediction process follows these steps:

1. Receive student academic input values.
2. Validate the supplied inputs.
3. Generate the required engineered features.
4. Load the selected trained model.
5. Load the saved preprocessing artifact.
6. Transform the input using the fitted preprocessor.
7. Preserve the transformed feature names.
8. Generate the predicted marks.
9. Return the prediction result.

The prediction output is an estimate, not a guaranteed academic result.

## 9. Model Persistence

StudentIQ uses Joblib to save and load trained machine learning artifacts.

Model files are stored in:

`models/`

The application loads these artifacts when performing predictions.

Model artifacts should be regenerated and evaluated whenever the underlying training data, preprocessing logic, or model configuration changes.

## 10. Testing

Automated tests are maintained in the `tests/` directory.

Run the test suite:

```bash
python -m pytest -v
```

Check dependency consistency:

```bash
python -m pip check
```

## 11. Important Considerations

- Model performance depends on the quality and representativeness of the training data.
- Predictions may contain errors.
- Evaluation metrics should be interpreted alongside the dataset and test methodology.
- Training and prediction must use compatible preprocessing logic.
- Student data must be handled responsibly.
- Personally identifiable student information should not be exposed publicly.

## 12. Future Improvements

Potential improvements include:

- Additional regression algorithms.
- Hyperparameter tuning.
- Cross-validation.
- Feature importance analysis.
- Prediction explainability.
- Model performance monitoring.
- More extensive model validation.

---

**Project:** StudentIQ  
**Developer:** Chandan Kumar  
**Brand:** CKMHTO.AI

*Turning Student Data into Intelligent Insights.*
