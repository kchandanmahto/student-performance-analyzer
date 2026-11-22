
<div align="center">

# CKMHTO.AI

**INNOVATION • INTELLIGENCE • TECHNOLOGY**

<br>

# StudentIQ

### Student Performance Analytics & Prediction Platform

**Turning Student Data into Intelligent Insights.**

<br>

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Pytest](https://img.shields.io/badge/Testing-Pytest-0A9EDC?logo=pytest&logoColor=white)](https://pytest.org/)
[![Deployment](https://img.shields.io/badge/Deployment-Live-success)](https://studentiq-ckmhto.streamlit.app/)

<br>

**A Data Science Product by CKMHTO.AI**

<br>

[Live Application](https://studentiq-ckmhto.streamlit.app/) ·
[Source Code](https://github.com/kchandanmahto/student-performance-analyzer) ·
[Developer Portfolio](https://ckmhto-ai.vercel.app/)

</div>

---

## Overview

**StudentIQ** is a Student Performance Analytics and Prediction Platform developed under the **CKMHTO.AI** brand.

The platform uses data science, statistical analysis, data visualization, and machine learning to transform academic records into meaningful insights.

It provides an interactive environment to explore student data, understand academic performance patterns, evaluate regression models, and estimate student marks using trained machine learning models.

## Live Application

Explore the deployed application:

**[Launch StudentIQ Dashboard →](https://studentiq-ckmhto.streamlit.app/)**

The application is deployed on Streamlit Community Cloud.

## Features

- Student dataset collection and management
- Data cleaning and missing-value handling
- Duplicate record detection and removal
- Exploratory Data Analysis (EDA)
- Academic feature engineering
- Data preprocessing and transformation
- Machine learning model training
- Student marks prediction
- Interactive analytics dashboard
- Model evaluation and comparison
- Dataset exploration
- Automated test coverage

## Platform Modules

| Module | Description |
|---|---|
| Data Collection | Collecting and managing student records |
| Data Cleaning | Handling missing values and duplicate records |
| Exploratory Data Analysis | Exploring distributions, trends, and relationships |
| Feature Engineering | Creating useful academic indicators |
| Data Preprocessing | Preparing features for machine learning |
| Model Training | Training regression models |
| Prediction Engine | Estimating student marks from input features |
| Model Evaluation | Measuring model performance |
| Interactive Dashboard | Presenting results and analytics through Streamlit |

## Technology Stack

| Area | Technology |
|---|---|
| Programming Language | Python 3.12 |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn, Plotly |
| Machine Learning | Scikit-learn |
| Dashboard | Streamlit |
| Model Persistence | Joblib |
| Testing | Pytest |
| Notebooks | Jupyter Notebook |
| Development Environment | Visual Studio Code |

## Machine Learning Models

StudentIQ currently includes two regression models for student marks prediction.

### 1. Linear Regression

A baseline regression algorithm that estimates student marks based on the selected academic features.

### 2. Random Forest Regressor

An ensemble learning algorithm that combines multiple decision trees to estimate student performance.

### Model Evaluation

The project uses the following regression evaluation metrics:

| Metric | Purpose |
|---|---|
| MAE | Measures average absolute prediction error |
| MSE | Measures average squared prediction error |
| RMSE | Measures prediction error on the target scale |
| R² Score | Measures the proportion of variance explained by the model |

Model evaluation results are available through the project's evaluation reports.

## Project Structure

```text
student-performance-analyzer/
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   └── PULL_REQUEST_TEMPLATE.md
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
├── docs/
│
├── models/
│   ├── linear_regression.joblib
│   ├── random_forest.joblib
│   └── preprocessor.joblib
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
├── pytest.ini
└── README.md
```

## Installation and Setup

### Prerequisites

- Python 3.12
- Git
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/kchandanmahto/student-performance-analyzer.git

cd student-performance-analyzer
```

### 2. Create a Virtual Environment

Windows PowerShell:

```powershell
python -m venv .venv

.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run main.py
```

Open the local URL displayed in the terminal.

## Testing

StudentIQ uses Pytest for automated testing.

Run the complete test suite:

```bash
python -m pytest -v
```

Check installed dependency consistency:

```bash
python -m pip check
```

## Documentation

Project documentation is available in the `docs/` directory.

- [System Architecture](docs/ARCHITECTURE.md)
- [Data Dictionary](docs/DATA_DICTIONARY.md)
- [Development Guide](docs/DEVELOPMENT.md)
- [Machine Learning](docs/MACHINE_LEARNING.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Testing Guide](docs/TESTING.md)
- [Contributing Guidelines](CONTRIBUTING.md)
- [Security Policy](SECURITY.md)
- [Support](SUPPORT.md)
- [Changelog](CHANGELOG.md)

## Data and Model Notes

The project uses student academic records for data analysis and model experimentation.

The trained models and preprocessing artifacts are stored using Joblib.

Use synthetic or properly anonymized student data when sharing datasets publicly. Do not upload personally identifiable student information.

Model predictions are estimates based on the available training data and input features. They should not be treated as guaranteed academic outcomes.

## Current Status

The StudentIQ dashboard is deployed and its prediction functionality is available through the live application.

The repository includes data processing modules, analysis notebooks, trained model artifacts, evaluation reports, automated tests, and project documentation.

## Project Information

| Field | Details |
|---|---|
| Product | StudentIQ |
| Category | Data Science & Machine Learning |
| Brand | CKMHTO.AI |
| Developer | Chandan Kumar |
| Language | Python |
| Interface | Streamlit |
| Repository | Public GitHub Project |
| Deployment | Streamlit Community Cloud |

## Developer

<div align="center">

### Chandan Kumar

**AI & Data Science Developer**

Building practical software solutions with data science, machine learning, and intelligent technologies.

[Portfolio](https://ckmhto-ai.vercel.app/) ·
[GitHub](https://github.com/kchandanmahto)

<br>

**CKMHTO.AI**

*Innovation • Intelligence • Technology*

</div>
