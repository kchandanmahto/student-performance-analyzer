import sys
from pathlib import Path

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.components.dashboard import render_dashboard


st.set_page_config(
    page_title="StudentIQ | Performance Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

render_dashboard()
