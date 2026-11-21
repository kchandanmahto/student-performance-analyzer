# Student Performance Analysis Report

## Dataset Overview

- Total students: 500
- Total columns: 7
- Missing values: 0

## Statistical Summary

|       |   attendance_percentage |   study_hours_per_day |   previous_marks |   assignment_score |   final_marks |
|:------|------------------------:|----------------------:|-----------------:|-------------------:|--------------:|
| count |                  500    |                500    |           500    |             500    |        500    |
| mean  |                   72.34 |                  5.24 |            65.32 |              68.22 |         70.28 |
| std   |                   15.63 |                  2.82 |            20.41 |              18.45 |         13.42 |
| min   |                   45.3  |                  0.51 |            30.04 |              35.04 |         40.03 |
| 25%   |                   58.22 |                  2.81 |            47.22 |              51.7  |         60.59 |
| 50%   |                   72.66 |                  5.19 |            64.47 |              67.48 |         69.72 |
| 75%   |                   86.04 |                  7.76 |            83.13 |              84.38 |         79.94 |
| max   |                   99.95 |                  9.99 |            99.96 |              99.92 |        100    |

## Correlation Analysis

|                       |   attendance_percentage |   study_hours_per_day |   previous_marks |   assignment_score |   final_marks |
|:----------------------|------------------------:|----------------------:|-----------------:|-------------------:|--------------:|
| attendance_percentage |                    1    |                 -0.07 |            -0.05 |              -0.01 |          0.24 |
| study_hours_per_day   |                   -0.07 |                  1    |            -0    |               0.05 |          0.65 |
| previous_marks        |                   -0.05 |                 -0    |             1    |              -0.01 |          0.5  |
| assignment_score      |                   -0.01 |                  0.05 |            -0.01 |               1    |          0.32 |
| final_marks           |                    0.24 |                  0.65 |             0.5  |               0.32 |          1    |

## Key Observations

- Average final marks: 70.28
- Highest final marks: 100.00
- Lowest final marks: 40.03
- Average attendance: 72.34%
- Average study hours: 5.24 hours/day

## Visualizations

See the `reports/figures/` folder for generated charts.
