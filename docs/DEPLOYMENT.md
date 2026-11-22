
# StudentIQ – Deployment Guide

## 1. Overview

StudentIQ is deployed using Streamlit Community Cloud and connected to its GitHub repository.

**Live Application:**

https://studentiq-ckmhto.streamlit.app/

**GitHub Repository:**

https://github.com/kchandanmahto/student-performance-analyzer

## 2. Deployment Requirements

Before deployment, ensure that the repository contains:

- Application entry point (`main.py`)
- Application modules
- `requirements.txt`
- Required model artifacts
- Required processed datasets
- Supporting project files

Do not include private student information, credentials, or confidential data in the public repository.

## 3. Streamlit Community Cloud Deployment

### Step 1: Open Streamlit Community Cloud

Visit:

https://share.streamlit.io/

Sign in using your GitHub account.

### Step 2: Connect GitHub Repository

Select the StudentIQ repository:

`kchandanmahto/student-performance-analyzer`

### Step 3: Configure Application

Set the application entry point to:

`main.py`

Select the appropriate branch:

`main`

### Step 4: Deploy

Start the deployment process and wait for the application to build.

Review deployment logs if any dependency or application errors occur.

## 4. Dependency Configuration

The project dependencies are defined in:

`requirements.txt`

Streamlit Community Cloud installs the required packages during deployment.

When dependencies change, update the requirements file and verify the application locally before pushing changes.

## 5. Updating the Deployed Application

The application is connected to the GitHub repository.

For future updates:

1. Make the required code changes locally.
2. Run the relevant tests.
3. Verify the application locally.
4. Commit the verified changes.
5. Push changes to the configured GitHub branch.
6. Check the Streamlit deployment status and logs.

When automatic deployment is enabled, Streamlit Community Cloud detects repository updates and rebuilds the application.

## 6. Deployment Verification

After deployment, verify:

- Application loads successfully.
- Dashboard pages are accessible.
- Required datasets are available.
- Trained models load correctly.
- Prediction functionality works.
- No critical errors appear in deployment logs.

## 7. Troubleshooting

### Dependency Errors

Check `requirements.txt` and verify dependencies locally.

```bash
python -m pip check
```

### Missing Files

Confirm that required datasets and model artifacts are available in the deployed repository.

### Application Errors

Review Streamlit deployment logs and reproduce the issue locally.

### Prediction Errors

Verify that the model and preprocessing artifacts are available and compatible with the application code.

## 8. Security and Data Privacy

- Never commit API keys or credentials.
- Never publish confidential student records.
- Use synthetic or anonymized datasets for public demonstrations.
- Review repository contents before deployment.
- Keep dependencies updated.

## 9. Deployment Links

| Resource | Link |
|---|---|
| Live Application | https://studentiq-ckmhto.streamlit.app/ |
| GitHub Repository | https://github.com/kchandanmahto/student-performance-analyzer |
| Streamlit Cloud | https://share.streamlit.io/ |
| Developer Portfolio | https://ckmhto-ai.vercel.app/ |

---

**Project:** StudentIQ  
**Developer:** Chandan Kumar  
**Brand:** CKMHTO.AI

*Turning Student Data into Intelligent Insights.*
