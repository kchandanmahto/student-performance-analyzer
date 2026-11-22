
# Contributing to StudentIQ

Thank you for your interest in contributing to **StudentIQ**, a student performance analytics and prediction platform developed under **CKMHTO.AI**.

Contributions that improve code quality, reliability, documentation, testing, and functionality are welcome.

## Getting Started

### 1. Fork the Repository

Fork the official repository:

https://github.com/kchandanmahto/student-performance-analyzer

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/student-performance-analyzer.git

cd student-performance-analyzer
```

### 3. Create a Virtual Environment

Windows PowerShell:

```powershell
python -m venv .venv

.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Development Guidelines

Please follow these guidelines when contributing:

- Write clean, readable, and maintainable Python code.
- Follow consistent naming conventions.
- Keep functions focused and reusable.
- Avoid unnecessary changes to existing functionality.
- Add or update tests when changing application behavior.
- Update documentation when introducing new features.
- Do not commit virtual environments, credentials, or private datasets.
- Use synthetic or anonymized data in public contributions.

## Testing

Run the existing test suite before submitting changes:

```bash
python -m pytest -v
```

Check dependency consistency:

```bash
python -m pip check
```

Make sure relevant tests pass before creating a pull request.

## Branching Guidelines

Create a separate branch for each feature or bug fix.

Examples:

```bash
git checkout -b feature/add-analytics
```

```bash
git checkout -b fix/prediction-error
```

## Commit Message Guidelines

Use clear and descriptive commit messages.

Examples:

- `feat: add student analytics feature`
- `fix: resolve prediction validation issue`
- `docs: improve project documentation`
- `test: add preprocessing test cases`
- `refactor: improve data cleaning module`

## Pull Request Process

1. Make your changes in a separate branch.
2. Run the relevant tests.
3. Review your changes before submitting.
4. Push your branch to your fork.
5. Open a Pull Request against the main branch.
6. Clearly describe the changes and their purpose.
7. Include relevant test results.

## Reporting Bugs

For bugs, use the repository's Bug Report issue template.

Include:

- A clear description of the issue.
- Steps to reproduce it.
- Expected behavior.
- Actual behavior.
- Relevant error messages.
- Environment details, when applicable.

## Suggesting Features

For feature suggestions, use the Feature Request issue template.

Explain the problem, proposed solution, and expected benefit.

## Questions and Support

For questions about contributing, open a GitHub issue with sufficient details.

Thank you for helping improve StudentIQ.

---

**StudentIQ**  
A Data Science Product by **CKMHTO.AI**

Developed by **Chandan Kumar**
