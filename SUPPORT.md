
# Support

## StudentIQ Support

Welcome to **StudentIQ**, a Student Performance Analytics and Prediction Platform developed under the **CKMHTO.AI** brand.

This document explains how users and contributors can get help with the project.

## Common Issues

Before requesting support, check the following:

### 1. Installation Issues

- Verify that Python 3.12 is installed.
- Make sure the virtual environment is activated.
- Install all dependencies from `requirements.txt`.
- Check dependency compatibility using:

```bash
python -m pip check
```

### 2. Application Startup Issues

Run the application using:

```bash
streamlit run main.py
```

Check the terminal output for error messages.

### 3. Prediction Issues

- Verify that the required model files are available.
- Check that the input values are valid.
- Confirm that the preprocessing artifacts are available.
- Review the error message displayed by the application.

### 4. Testing Issues

Run the automated test suite:

```bash
python -m pytest -v
```

## Getting Help

If you encounter an issue:

1. Check the project README.
2. Review the existing GitHub issues.
3. Search for a similar reported problem.
4. Open a new GitHub issue if the problem remains unresolved.

GitHub Issues:

https://github.com/kchandanmahto/student-performance-analyzer/issues

## Reporting a Problem

When creating a support request, include:

- A clear description of the problem.
- Steps to reproduce the issue.
- Expected and actual behavior.
- Python version and operating system.
- Relevant error messages.
- Screenshots, if useful and safe to share.

Do not include passwords, API keys, or private student information.

## Feature Suggestions

Suggestions for improving StudentIQ are welcome.

Use the GitHub Feature Request template and explain the purpose and expected benefit of your suggestion.

## Security Issues

Do not report security vulnerabilities through public GitHub issues.

Follow the instructions in [SECURITY.md](SECURITY.md) for responsible security reporting.

## Project Links

- **Live Application:** https://studentiq-ckmhto.streamlit.app/
- **GitHub Repository:** https://github.com/kchandanmahto/student-performance-analyzer
- **Developer Portfolio:** https://ckmhto-ai.vercel.app/

---

**Project:** StudentIQ  
**Developer:** Chandan Kumar  
**Brand:** CKMHTO.AI

*Turning Student Data into Intelligent Insights.*
