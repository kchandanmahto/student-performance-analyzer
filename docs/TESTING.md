
# StudentIQ – Testing Documentation

## 1. Overview

StudentIQ uses Pytest to verify important application components and maintain code reliability.

The project includes automated tests for data cleaning, preprocessing, and student performance prediction.

## 2. Testing Framework

| Tool | Purpose |
|---|---|
| Pytest | Automated test execution |
| Python | Test execution environment |
| Scikit-learn | Machine learning component validation |

## 3. Test Directory

Automated tests are maintained in the `tests/` directory.

Current test modules:

| Test File | Testing Area |
|---|---|
| `test_cleaning.py` | Data cleaning functionality |
| `test_preprocessing.py` | Data preprocessing functionality |
| `test_prediction.py` | Student performance prediction |

## 4. Environment Setup

Activate the project's virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## 5. Running Tests

### Run All Tests

```powershell
python -m pytest -v
```

### Run a Specific Test Module

Data cleaning:

```powershell
python -m pytest -v tests/test_cleaning.py
```

Data preprocessing:

```powershell
python -m pytest -v tests/test_preprocessing.py
```

Prediction:

```powershell
python -m pytest -v tests/test_prediction.py
```

### Run Tests with a Summary

```powershell
python -m pytest -ra
```

## 6. Dependency Verification

Check whether installed packages have dependency conflicts:

```powershell
python -m pip check
```

## 7. Test Configuration

The project uses `pytest.ini` to configure test discovery and execution.

Configuration:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -ra --import-mode=importlib
```

## 8. Continuous Integration

GitHub Actions is configured to run automated tests when changes are pushed to the `main` branch or when a Pull Request targets `main`.

Workflow file:

`.github/workflows/tests.yml`

The workflow performs:

1. Repository checkout.
2. Python environment setup.
3. Dependency installation.
4. Dependency consistency check.
5. Automated test execution.

## 9. Testing Guidelines

When modifying StudentIQ:

- Run the relevant tests before submitting changes.
- Add tests for new functionality.
- Update existing tests when behavior changes.
- Investigate failures instead of ignoring them.
- Avoid committing temporary test files.
- Verify the application after significant changes.

## 10. Test Results

Record test results using actual execution output.

Do not report a test as passed unless it has been executed successfully.

## 11. Future Testing Improvements

Potential improvements include:

- Additional unit tests.
- Integration testing.
- Dashboard component testing.
- Test coverage reporting.
- Data validation tests.
- Model performance regression tests.

---

**Project:** StudentIQ  
**Developer:** Chandan Kumar  
**Brand:** CKMHTO.AI

*Turning Student Data into Intelligent Insights.*
