
# StudentIQ – Data Dictionary

## 1. Introduction

This document describes the datasets and features used in StudentIQ, a Student Performance Analytics and Prediction Platform developed under the CKMHTO.AI brand.

It explains the meaning and role of the columns available in the cleaned, engineered, and machine learning datasets.

## 2. Cleaned Dataset

**File:** `data/processed/cleaned_students.csv`

The cleaned dataset contains student identifiers, academic attributes, and final marks.

| Column | Description | Data Type |
|---|---|---|
| student_id | Unique identifier assigned to a student record | String |
| student_name | Student display name | String |
| attendance_percentage | Student attendance percentage | Float |
| study_hours_per_day | Average study hours per day | Float |
| previous_marks | Marks obtained in previous academic performance | Float |
| assignment_score | Student assignment score | Float |
| final_marks | Final academic marks used as the prediction target | Float |

## 3. Engineered Dataset

**File:** `data/processed/engineered_students.csv`

The engineered dataset contains the original academic attributes and additional features created during feature engineering.

| Column | Description | Data Type |
|---|---|---|
| student_id | Unique student identifier | String |
| student_name | Student display name | String |
| attendance_percentage | Attendance percentage | Float |
| study_hours_per_day | Average daily study hours | Float |
| previous_marks | Previous academic marks | Float |
| assignment_score | Assignment score | Float |
| final_marks | Final marks and prediction target | Float |
| internal_average | Derived academic average indicator | Float |
| attendance_category | Categorized attendance level | Categorical |
| study_category | Categorized study-hours level | Categorical |
| academic_engagement_score | Derived academic engagement indicator | Float |
| previous_performance | Categorized previous academic performance | Categorical |

### Engineered Feature Descriptions

**internal_average**

A derived feature representing an academic average indicator.

**attendance_category**

Categorical representation of attendance levels, including:

- High
- Medium
- Low

**study_category**

Categorical representation of study-hour levels, including:

- High
- Medium
- Low

**academic_engagement_score**

A derived numerical indicator representing academic engagement.

**previous_performance**

Categorical representation of previous academic performance, including:

- Poor
- Average
- Good
- Excellent

The exact calculation formulas and category thresholds are defined by the feature engineering implementation.

## 4. Machine Learning Dataset

**Files:**
- `data/processed/train_data.csv`
- `data/processed/test_data.csv`

These datasets contain transformed numerical and categorical features prepared for machine learning.

### Numerical Features

| Feature | Description |
|---|---|
| num__attendance_percentage | Transformed attendance percentage |
| num__study_hours_per_day | Transformed study hours |
| num__previous_marks | Transformed previous marks |
| num__assignment_score | Transformed assignment score |
| num__internal_average | Transformed internal average |
| num__academic_engagement_score | Transformed engagement score |

### Categorical Features

Categorical variables are converted into numerical indicator columns through preprocessing.

| Feature Group | Available Categories |
|---|---|
| attendance_category | High, Low, Medium |
| study_category | High, Low, Medium |
| previous_performance | Average, Excellent, Good, Poor |

The transformed columns use the `cat__` prefix.

### Target Variable

| Column | Description |
|---|---|
| final_marks | Student final marks used as the regression target |

## 5. Data Preprocessing

StudentIQ uses preprocessing artifacts to prepare input data for machine learning.

The preprocessing process includes:

- Numerical feature transformation.
- Categorical feature encoding.
- Consistent feature preparation for model training and prediction.
- Reuse of the saved preprocessing artifact.

The saved preprocessing artifact is:

`models/preprocessor.joblib`

## 6. Data Types

The project uses the following general data types:

| Data Type | Purpose |
|---|---|
| String | Student identifiers and names |
| Float | Academic measurements and scores |
| Categorical | Attendance, study, and performance categories |
| Encoded Numerical | Machine learning input features |

## 7. Data Privacy

Student academic records may contain sensitive personal information.

Follow these practices:

- Do not publish personally identifiable student information.
- Use synthetic or anonymized records for public demonstrations.
- Avoid committing confidential datasets to GitHub.
- Restrict access to private student records.
- Do not expose student information in application logs.

## 8. Important Notes

- `final_marks` is the prediction target.
- Student identifiers and names are descriptive fields, not model input features in the transformed training dataset.
- Transformed feature names are generated by the saved preprocessing pipeline.
- Category thresholds and feature calculation formulas should be referenced from the feature engineering source code.
- Data descriptions do not imply that every dataset contains real student records.

---

**Project:** StudentIQ  
**Developer:** Chandan Kumar  
**Brand:** CKMHTO.AI

*Turning Student Data into Intelligent Insights.*
