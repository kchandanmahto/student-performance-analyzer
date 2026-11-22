
# StudentIQ – Development Guide

## 1. Introduction

This guide explains how to set up, run, test, and contribute to StudentIQ locally.

**Project:** StudentIQ  
**Brand:** CKMHTO.AI  
**Developer:** Chandan Kumar

## 2. Development Requirements

Install the following tools before starting development:

- Python 3.12
- Git
- Visual Studio Code (recommended)
- pip

## 3. Clone the Repository

Open PowerShell and execute:

```powershell
git clone https://github.com/kchandanmahto/student-performance-analyzer.git

cd student-performance-analyzer
```

## 4. Create a Virtual Environment

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 5. Install Dependencies

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install project dependencies:

```powershell
pip install -r requirements.txt
```

Verify installed dependencies:

```powershell
python -m pip check
```

## 6. Run the Application

Start the Streamlit application:

```powershell
streamlit run main.py
```

Open the local URL displayed in the terminal.

## 7. Project Development Workflow

Follow these steps when working on the project:

1. Understand the existing module before modifying it.
2. Identify the required changes.
3. Keep code modular and maintainable.
4. Avoid unrelated modifications.
5. Update relevant tests.
6. Run the automated test suite.
7. Review the final code changes.
8. Commit and push verified changes.

## 8. Run Automated Tests

Execute all project tests:

```powershell
python -m pytest -v
```

Check dependency consistency:

```powershell
python -m pip check
```

## 9. Git Development Workflow

Check the current Git status:

```powershell
git status
```

Create a feature branch:

```powershell
git checkout -b feature/your-feature-name
```

Stage specific changes:

```powershell
git add <file-path>
```

Commit changes:

```powershell
git commit -m "feat: describe your changes"
```

Push the branch:

```powershell
git push origin feature/your-feature-name
```

Submit a Pull Request through GitHub when contributing to the main repository.

## 10. Coding Guidelines

- Use meaningful variable and function names.
- Follow consistent Python formatting.
- Keep functions focused and reusable.
- Handle invalid inputs appropriately.
- Avoid unnecessary dependencies.
- Preserve existing application behavior.
- Add tests for new functionality.
- Update documentation when required.

## 11. Data and Model Management

StudentIQ uses processed datasets and saved machine learning artifacts.

Important project locations:

- `data/raw/` – Raw input datasets.
- `data/processed/` – Processed datasets.
- `models/` – Saved machine learning models and preprocessing artifacts.
- `reports/` – Analysis and evaluation reports.

Do not commit private student records, credentials, or confidential information.

## 12. Development Troubleshooting

### Python Environment Issues

Verify Python:

```powershell
python --version
```

Verify pip:

```powershell
python -m pip --version
```

### Missing Dependencies

```powershell
pip install -r requirements.txt
```

### Application Startup Issues

```powershell
streamlit run main.py
```

Review terminal errors and verify that required project files exist.

### Test Failures

```powershell
python -m pytest -v
```

Review the failing test and its associated error message before modifying code.

## 13. Useful Project Links

- Live Application: https://studentiq-ckmhto.streamlit.app/
- GitHub Repository: https://github.com/kchandanmahto/student-performance-analyzer
- Developer Portfolio: https://ckmhto-ai.vercel.app/

---

**StudentIQ**

A Data Science Product by **CKMHTO.AI**

Developed by **Chandan Kumar**

*Turning Student Data into Intelligent Insights.*
