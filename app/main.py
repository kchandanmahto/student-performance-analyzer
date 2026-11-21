import sys
from pathlib import Path

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.components.dashboard import render_dashboard


st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


with st.sidebar:
    st.title("📊 SPA Dashboard")
    st.write("Student Performance Analyzer")
    st.divider()
    st.info(
        "A Data Science project covering data collection, "
        "analysis, preprocessing and machine learning."
    )


render_dashboard()
