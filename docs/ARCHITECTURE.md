
# StudentIQ – System Architecture

## 1. Introduction

StudentIQ is a Student Performance Analytics and Prediction Platform developed under the CKMHTO.AI brand.

The system uses Python, data processing libraries, machine learning algorithms, and Streamlit to analyze student academic records and estimate student marks.

This document describes the project's architecture, major components, and data flow.

## 2. Architecture Overview

StudentIQ follows a modular data science application architecture.

The main components are:

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Data Preprocessing
6. Model Training
7. Model Evaluation
8. Prediction Engine
9. Interactive Dashboard

## 3. High-Level Architecture

```text
             STUDENT DATA
                   |
                   v
           DATA COLLECTION
                   |
                   v
             DATA CLEANING
                   |
                   v
        EXPLORATORY DATA ANALYSIS
                   |
                   v
          FEATURE ENGINEERING
                   |
                   v
          DATA PREPROCESSING
                   |
                   v
            MODEL TRAINING
                   |
                   v
            MODEL EVALUATION
                   |
                   v
           TRAINED ML MODELS
                   |
                   v
          PREDICTION ENGINE
                   |
                   v
          STREAMLIT DASHBOARD
                   |
                   v
           ANALYTICAL INSIGHTS
```

## 4. Technology Architecture

### Programming Language
- Python 3.12

### Data Processing
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn
- Plotly

### Machine Learning
- Scikit-learn

### Application Interface
- Streamlit

### Model Storage
- Joblib

### Testing
- Pytest

## 5. Main Components

### 5.1 Data Collection

Responsible for collecting and managing student academic records.

Source file:

`src/data/collection.py`

### 5.2 Data Cleaning

Handles data quality operations such as:

- Missing-value handling
- Duplicate record detection
- Data validation
- Dataset preparation

Source file:

`src/data/cleaning.py`

### 5.3 Exploratory Data Analysis

Analyzes student data to understand distributions, trends, and relationships.

Source file:

`src/analysis/eda.py`

### 5.4 Feature Engineering

Creates additional academic indicators from existing student attributes.

Source file:

`src/features/engineering.py`

### 5.5 Data Preprocessing

Prepares dataset features for machine learning using preprocessing and transformation techniques.

### 5.6 Model Training

Trains regression models using prepared student data.

Source file:

`src/models/train.py`

Current models:

- Linear Regression
- Random Forest Regressor

### 5.7 Model Evaluation

Measures prediction performance using regression metrics.

Source file:

`src/models/evaluate.py`

Metrics:

- MAE
- MSE
- RMSE
- R² Score

### 5.8 Prediction Engine

Accepts student academic inputs, applies the saved preprocessing pipeline, and generates estimated marks using trained models.

Source file:

`src/models/predict.py`

### 5.9 Dashboard

Provides an interactive interface for exploring student analytics and predictions.

Main application files:

- `main.py`
- `app/main.py`
- `app/components/dashboard.py`

## 6. Data Flow

The project data flow can be understood in the following stages:

1. Student records are collected.
2. Data cleaning prepares the records.
3. Exploratory analysis identifies patterns.
4. Feature engineering creates additional indicators.
5. Preprocessing transforms model input features.
6. Regression models are trained.
7. Evaluation metrics measure model performance.
8. Trained models and preprocessing artifacts are saved.
9. The prediction engine loads the saved artifacts.
10. The dashboard presents analytics and prediction results.

## 7. Project Directory Structure

```text
student-performance-analyzer/
│
├── app/
│   ├── main.py
│   └── components/
│       └── dashboard.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── notebooks/
│
├── reports/
│
├── src/
│   ├── analysis/
│   ├── data/
│   ├── features/
│   ├── models/
│   └── visualization/
│
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
```

## 8. Deployment Architecture

The interactive application is deployed using Streamlit Community Cloud.

Live application:

https://studentiq-ckmhto.streamlit.app/

Source repository:

https://github.com/kchandanmahto/student-performance-analyzer

## 9. Testing Architecture

Pytest is used to verify important project functionality.

Test modules include:

- Data cleaning tests
- Preprocessing tests
- Prediction tests

Run tests:

```bash
python -m pytest -v
```

## 10. Design Principles

StudentIQ follows these development principles:

- Modular and maintainable code
- Separation of responsibilities
- Reusable data processing components
- Consistent preprocessing between training and prediction
- Automated testing
- Responsible handling of student data
- Clear technical documentation

## 11. Future Improvements

Potential future improvements include:

- Expanded model experimentation
- More advanced academic performance indicators
- Improved prediction explainability
- Enhanced dashboard analytics
- Additional data validation
- Expanded automated test coverage

---

**Project:** StudentIQ  
**Developer:** Chandan Kumar  
**Brand:** CKMHTO.AI

*Turning Student Data into Intelligent Insights.*
