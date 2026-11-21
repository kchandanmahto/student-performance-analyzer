from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from src.models.predict import predict_student_performance


ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = ROOT / "data" / "processed" / "cleaned_students.csv"
EVALUATION_PATH = ROOT / "reports" / "model_evaluation.csv"

BG = "#0B1020"
CARD = "#121A2D"
BLUE = "#4F8CFF"
PURPLE = "#8B5CF6"
TEXT = "#F1F5F9"
MUTED = "#94A3B8"


def load_dataset():
    if DATA_PATH.exists():
        return pd.read_csv(DATA_PATH)
    return pd.DataFrame()


def load_evaluation():
    if EVALUATION_PATH.exists():
        return pd.read_csv(EVALUATION_PATH)
    return pd.DataFrame()


def inject_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 10% 0%, #17264a 0%, transparent 30%),
            #0B1020;
        color: #F1F5F9;
    }

    [data-testid="stSidebar"] {
        background: #0E1628;
        border-right: 1px solid #26334D;
    }

    [data-testid="stSidebar"] > div {
        padding-top: 2rem;
    }

    .brand {
        font-size: 24px;
        font-weight: 800;
        letter-spacing: -1px;
        color: #F8FAFC;
        margin-bottom: 4px;
    }

    .brand span {
        color: #60A5FA;
    }

    .brand-subtitle {
        font-size: 11px;
        color: #94A3B8;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .hero {
        background: linear-gradient(120deg, #172B50, #24204B);
        border: 1px solid #34476E;
        border-radius: 22px;
        padding: 30px;
        margin-bottom: 26px;
        position: relative;
        overflow: hidden;
    }

    .hero h1 {
        color: white;
        font-size: 32px;
        font-weight: 800;
        margin: 0;
        letter-spacing: -1.2px;
    }

    .hero p {
        color: #C4D4F0;
        margin: 10px 0 0 0;
        font-size: 14px;
    }

    .hero-tag {
        display: inline-block;
        background: #284B7D;
        color: #BBD8FF;
        padding: 6px 12px;
        border-radius: 30px;
        font-size: 11px;
        font-weight: 700;
        margin-bottom: 15px;
        letter-spacing: 1px;
    }

    .section-heading {
        font-size: 20px;
        font-weight: 700;
        color: #F8FAFC;
        margin: 20px 0 5px 0;
    }

    .section-description {
        font-size: 12px;
        color: #94A3B8;
        margin-bottom: 18px;
    }

    .metric-card {
        background: linear-gradient(145deg, #17243C, #111A2C);
        border: 1px solid #293B5C;
        border-radius: 17px;
        padding: 20px;
        min-height: 125px;
    }

    .metric-label {
        color: #9FB0CA;
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 12px;
    }

    .metric-value {
        color: #FFFFFF;
        font-size: 29px;
        font-weight: 800;
        letter-spacing: -1px;
    }

    .metric-note {
        color: #60A5FA;
        font-size: 11px;
        margin-top: 7px;
    }

    .panel {
        background: #111B2D;
        border: 1px solid #293B5C;
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 18px;
    }

    .result-card {
        background: linear-gradient(135deg, #172F55, #30235C);
        border: 1px solid #5264A5;
        border-radius: 20px;
        padding: 25px;
        margin-top: 20px;
        text-align: center;
    }

    .result-label {
        color: #C5D5F5;
        font-size: 13px;
    }

    .result-value {
        color: #FFFFFF;
        font-size: 48px;
        font-weight: 800;
        margin: 10px 0;
    }

    .result-model {
        color: #A5C8FF;
        font-size: 12px;
    }

    div[data-testid="stForm"] {
        background: #111B2D;
        border: 1px solid #293B5C;
        border-radius: 18px;
        padding: 22px;
    }

    .stButton > button,
    div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(90deg, #3478F6, #7855E8);
        color: white;
        border: none;
        border-radius: 10px;
        min-height: 44px;
        font-weight: 700;
        transition: 0.2s ease;
    }

    .stButton > button:hover,
    div[data-testid="stFormSubmitButton"] > button:hover {
        border: 1px solid #8AB8FF;
        color: white;
        filter: brightness(1.12);
    }

    .stTextInput input,
    .stNumberInput input {
        background: #18243A;
        color: white;
        border: 1px solid #344766;
        border-radius: 9px;
    }

    div[data-baseweb="select"] > div {
        background: #18243A;
        border-color: #344766;
    }

    [data-testid="stDataFrame"] {
        border: 1px solid #293B5C;
        border-radius: 12px;
        overflow: hidden;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header[data-testid="stHeader"] {
        background: transparent;
    }

    @media (max-width: 768px) {
        .hero { padding: 21px; }
        .hero h1 { font-size: 24px; }
        .metric-card { padding: 15px; }
        .metric-value { font-size: 24px; }
        .result-value { font-size: 36px; }
    }
    </style>
    """, unsafe_allow_html=True)


def render_hero(title, subtitle, tag):
    st.markdown(f"""
    <div class="hero">
        <div class="hero-tag">{tag}</div>
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


def render_metric(label, value, note):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-note">{note}</div>
    </div>
    """, unsafe_allow_html=True)


def section_heading(title, description):
    st.markdown(
        f'<div class="section-heading">{title}</div>'
        f'<div class="section-description">{description}</div>',
        unsafe_allow_html=True
    )


def chart_layout(fig, height=350):
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=TEXT, family="Inter"),
        margin=dict(l=15, r=15, t=35, b=15),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(color=MUTED)
        ),
        xaxis=dict(
            gridcolor="#26344D",
            zerolinecolor="#26344D"
        ),
        yaxis=dict(
            gridcolor="#26344D",
            zerolinecolor="#26344D"
        )
    )
    return fig


def show_overview(df, results):
    render_hero(
        "Student Performance Overview",
        "Your central workspace for academic analytics and machine learning insights.",
        "DATA INTELLIGENCE • OVERVIEW"
    )

    if df.empty:
        st.warning("Cleaned dataset not found. Run the data pipeline first.")
        return

    total = len(df)
    average = df["final_marks"].mean()
    attendance = df["attendance_percentage"].mean()
    study = df["study_hours_per_day"].mean()

    cols = st.columns(4)

    metrics = [
        ("TOTAL STUDENTS", f"{total:,}", "Records analyzed"),
        ("AVERAGE MARKS", f"{average:.2f}", "Out of 100"),
        ("AVERAGE ATTENDANCE", f"{attendance:.1f}%", "Attendance rate"),
        ("DAILY STUDY HOURS", f"{study:.1f}h", "Average per student"),
    ]

    for col, metric in zip(cols, metrics):
        with col:
            render_metric(*metric)

    st.write("")
    section_heading(
        "Academic Performance Analytics",
        "Explore marks distribution and academic relationships."
    )

    left, right = st.columns(2)

    with left:
        fig = px.histogram(
            df,
            x="final_marks",
            nbins=20,
            title="Final Marks Distribution",
            color_discrete_sequence=[BLUE]
        )
        fig.update_traces(marker_line_width=0)
        st.plotly_chart(chart_layout(fig), use_container_width=True)

    with right:
        fig = px.scatter(
            df,
            x="study_hours_per_day",
            y="final_marks",
            color="attendance_percentage",
            title="Study Hours vs Final Marks",
            color_continuous_scale="Blues",
            hover_data=["previous_marks", "assignment_score"]
        )
        st.plotly_chart(chart_layout(fig), use_container_width=True)

    section_heading(
        "Model Snapshot",
        "Current evaluation results from the held-out test dataset."
    )

    if not results.empty:
        best = results.loc[results["MAE"].idxmin()]

        cols = st.columns(3)

        with cols[0]:
            render_metric("BEST MODEL", best["Model"], "Lowest MAE")

        with cols[1]:
            render_metric("MAE", f"{best['MAE']:.3f}", "Lower is better")

        with cols[2]:
            render_metric("R² SCORE", f"{best['R2 Score']:.3f}", "Higher is better")


def show_predictions():
    render_hero(
        "Student Performance Prediction",
        "Enter academic details and generate an estimated final marks prediction.",
        "MACHINE LEARNING • PREDICTION"
    )

    section_heading(
        "Student Academic Profile",
        "Provide the following information to run the trained ML model."
    )

    with st.form("premium_prediction_form"):
        col1, col2 = st.columns(2)

        with col1:
            attendance = st.number_input(
                "Attendance Percentage",
                min_value=0.0,
                max_value=100.0,
                value=85.0,
                step=1.0
            )

            study_hours = st.number_input(
                "Study Hours Per Day",
                min_value=0.0,
                max_value=24.0,
                value=5.0,
                step=0.5
            )

        with col2:
            previous_marks = st.number_input(
                "Previous Examination Marks",
                min_value=0.0,
                max_value=100.0,
                value=75.0,
                step=1.0
            )

            assignment_score = st.number_input(
                "Assignment Score",
                min_value=0.0,
                max_value=100.0,
                value=80.0,
                step=1.0
            )

        model_name = st.selectbox(
            "Choose Prediction Model",
            ["Linear Regression", "Random Forest"]
        )

        submitted = st.form_submit_button(
            "Generate Performance Prediction",
            use_container_width=True
        )

    if submitted:
        model_choice = "1" if model_name == "Linear Regression" else "2"

        try:
            result = predict_student_performance(
                attendance,
                study_hours,
                previous_marks,
                assignment_score,
                model_choice
            )

            st.markdown(f"""
            <div class="result-card">
                <div class="result-label">PREDICTED FINAL MARKS</div>
                <div class="result-value">{result['predicted_marks']}<span style="font-size:20px"> / 100</span></div>
                <div class="result-model">MODEL: {result['model'].upper()}</div>
            </div>
            """, unsafe_allow_html=True)

            st.progress(
                int(round(result["predicted_marks"])),
                text="Predicted marks on a 100-point scale"
            )

            st.info(
                "This is a model-based estimate using synthetic training data. "
                "It is not a guarantee of actual examination performance."
            )

        except (ValueError, FileNotFoundError) as error:
            st.error(str(error))



def show_analytics(df):
    render_hero(
        "Academic Analytics",
        "Discover student performance patterns, academic trends and data-driven insights.",
        "DATA INTELLIGENCE • ANALYTICS"
    )

    if df.empty:
        st.warning("Cleaned dataset not found. Run the data pipeline first.")
        return

    required = [
        "attendance_percentage",
        "study_hours_per_day",
        "previous_marks",
        "assignment_score",
        "final_marks",
    ]

    missing = [column for column in required if column not in df.columns]

    if missing:
        st.error(f"Required dataset columns missing: {missing}")
        return

    section_heading(
        "Performance Overview",
        "Explore key academic indicators from the student dataset."
    )

    col1, col2 = st.columns(2)

    with col1:
        pass_threshold = st.slider(
            "Minimum marks threshold",
            min_value=0,
            max_value=100,
            value=40,
            help="This threshold is configurable for this analysis."
        )

    with col2:
        minimum_attendance = st.slider(
            "Minimum attendance filter (%)",
            min_value=0,
            max_value=100,
            value=0
        )

    filtered = df[
        df["attendance_percentage"] >= minimum_attendance
    ].copy()

    if filtered.empty:
        st.warning("No student records match the selected attendance filter.")
        return

    pass_rate = (
        filtered["final_marks"] >= pass_threshold
    ).mean() * 100

    cols = st.columns(4)

    with cols[0]:
        render_metric(
            "ANALYZED STUDENTS",
            f"{len(filtered):,}",
            "Filtered records"
        )

    with cols[1]:
        render_metric(
            "AVERAGE MARKS",
            f"{filtered['final_marks'].mean():.2f}",
            "Out of 100"
        )

    with cols[2]:
        render_metric(
            "PASS RATE",
            f"{pass_rate:.1f}%",
            f"Threshold: {pass_threshold} marks"
        )

    with cols[3]:
        render_metric(
            "MEDIAN MARKS",
            f"{filtered['final_marks'].median():.2f}",
            "Middle performance"
        )

    st.write("")

    section_heading(
        "Marks Distribution",
        "Understand how final marks are distributed among students."
    )

    left, right = st.columns(2)

    with left:
        fig = px.histogram(
            filtered,
            x="final_marks",
            nbins=20,
            title="Final Marks Distribution",
            color_discrete_sequence=[BLUE],
            marginal="box"
        )
        st.plotly_chart(
            chart_layout(fig),
            use_container_width=True
        )

    with right:
        fig = px.box(
            filtered,
            y="final_marks",
            title="Final Marks Spread",
            color_discrete_sequence=[PURPLE]
        )
        st.plotly_chart(
            chart_layout(fig),
            use_container_width=True
        )

    section_heading(
        "Academic Performance Relationships",
        "Explore how attendance, study hours and previous marks relate to final marks."
    )

    left, right = st.columns(2)

    with left:
        fig = px.scatter(
            filtered,
            x="attendance_percentage",
            y="final_marks",
            color="study_hours_per_day",
            title="Attendance vs Final Marks",
            color_continuous_scale="Blues",
            hover_data=["previous_marks", "assignment_score"]
        )
        st.plotly_chart(
            chart_layout(fig),
            use_container_width=True
        )

    with right:
        fig = px.scatter(
            filtered,
            x="study_hours_per_day",
            y="final_marks",
            color="attendance_percentage",
            title="Study Hours vs Final Marks",
            color_continuous_scale="Purples",
            hover_data=["previous_marks", "assignment_score"]
        )
        st.plotly_chart(
            chart_layout(fig),
            use_container_width=True
        )

    section_heading(
        "Performance by Attendance Group",
        "Compare marks across attendance categories."
    )

    grouped = filtered.copy()

    grouped["attendance_group"] = pd.cut(
        grouped["attendance_percentage"],
        bins=[-1, 60, 75, 100],
        labels=["Low", "Medium", "High"]
    )

    fig = px.box(
        grouped,
        x="attendance_group",
        y="final_marks",
        color="attendance_group",
        category_orders={
            "attendance_group": ["Low", "Medium", "High"]
        },
        title="Marks by Attendance Group",
        color_discrete_sequence=[BLUE, PURPLE, "#14B8A6"]
    )

    st.plotly_chart(
        chart_layout(fig),
        use_container_width=True
    )

    section_heading(
        "Feature Correlation",
        "Measure linear relationships between numeric academic features."
    )

    numeric_columns = [
        "attendance_percentage",
        "study_hours_per_day",
        "previous_marks",
        "assignment_score",
        "final_marks"
    ]

    correlation = filtered[numeric_columns].corr()

    fig = px.imshow(
        correlation,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        zmin=-1,
        zmax=1,
        title="Academic Feature Correlation Heatmap"
    )

    st.plotly_chart(
        chart_layout(fig, height=480),
        use_container_width=True
    )

    relationships = (
        correlation["final_marks"]
        .drop("final_marks")
        .sort_values(key=abs, ascending=False)
    )

    strongest_feature = relationships.index[0]
    strongest_value = relationships.iloc[0]

    st.info(
        f"Strongest absolute linear correlation with final marks in "
        f"the filtered dataset: {strongest_feature} "
        f"({strongest_value:.3f}). Correlation does not establish causation."
    )

    section_heading(
        "Filtered Student Records",
        "Inspect the records included in this analytics view."
    )

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )
def show_model_analytics(results):
    render_hero(
        "Model Performance Analytics",
        "Compare trained machine learning algorithms using standard regression metrics.",
        "MODEL INTELLIGENCE • EVALUATION"
    )

    if results.empty:
        st.warning("Evaluation report not found. Run model evaluation first.")
        return

    best = results.loc[results["MAE"].idxmin()]

    cols = st.columns(3)

    with cols[0]:
        render_metric("BEST MODEL", best["Model"], "Based on lowest MAE")

    with cols[1]:
        render_metric("BEST MAE", f"{best['MAE']:.4f}", "Lower is better")

    with cols[2]:
        render_metric("BEST R²", f"{best['R2 Score']:.4f}", "Higher is better")

    section_heading(
        "Metric Comparison",
        "Evaluate prediction error and explained variance across models."
    )

    left, right = st.columns(2)

    with left:
        fig = px.bar(
            results,
            x="Model",
            y="MAE",
            color="Model",
            title="Mean Absolute Error",
            color_discrete_sequence=[BLUE, PURPLE],
            text_auto=".3f"
        )
        st.plotly_chart(chart_layout(fig), use_container_width=True)

    with right:
        fig = px.bar(
            results,
            x="Model",
            y="R2 Score",
            color="Model",
            title="R² Score",
            color_discrete_sequence=[PURPLE, BLUE],
            text_auto=".3f"
        )
        st.plotly_chart(chart_layout(fig), use_container_width=True)

    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.subheader("Detailed Evaluation Results")
    st.dataframe(
        results.round(4),
        use_container_width=True,
        hide_index=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.caption(
        "MAE, MSE and RMSE are error metrics (lower is better). "
        "R² measures explained variance (higher is better)."
    )


def show_dataset_explorer(df):
    render_hero(
        "Dataset Explorer",
        "Explore the cleaned student dataset and inspect academic records.",
        "DATA INTELLIGENCE • EXPLORER"
    )

    if df.empty:
        st.warning("Cleaned dataset not found.")
        return

    section_heading(
        "Filter Student Records",
        "Filter records by marks and attendance."
    )

    col1, col2 = st.columns(2)

    with col1:
        min_marks = st.slider(
            "Minimum Final Marks",
            0,
            100,
            0
        )

    with col2:
        min_attendance = st.slider(
            "Minimum Attendance",
            0,
            100,
            0
        )

    filtered = df[
        (df["final_marks"] >= min_marks)
        & (df["attendance_percentage"] >= min_attendance)
    ]

    cols = st.columns(3)

    with cols[0]:
        render_metric("FILTERED RECORDS", str(len(filtered)), "Matching students")

    with cols[1]:
        value = filtered["final_marks"].mean() if not filtered.empty else 0
        render_metric("FILTERED AVG MARKS", f"{value:.2f}", "Out of 100")

    with cols[2]:
        value = filtered["attendance_percentage"].mean() if not filtered.empty else 0
        render_metric("FILTERED ATTENDANCE", f"{value:.1f}%", "Average attendance")

    st.write("")
    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )

    csv = filtered.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Filtered Dataset",
        data=csv,
        file_name="student_performance_filtered.csv",
        mime="text/csv"
    )


def render_dashboard():
    inject_custom_css()

    df = load_dataset()
    results = load_evaluation()

    with st.sidebar:
        st.markdown("""
        <div class="brand">STUDENT<span>IQ</span></div>
        <div class="brand-subtitle">Performance Intelligence</div>
        """, unsafe_allow_html=True)

        st.write("")
        st.divider()

        page = st.radio(
            "WORKSPACE",
            [
                "Overview",
                "Analytics",
                "Predictions",
                "Model Analytics",
                "Dataset Explorer"
            ],
            label_visibility="visible"
        )

        st.divider()

        st.markdown("**PROJECT STATUS**")
        st.caption("Data Science • Machine Learning")
        st.caption("Version 1.0.0")

        st.write("")
        st.caption("Built with Python & Streamlit")

    if page == "Overview":
        show_overview(df, results)

    elif page == "Analytics":
        show_analytics(df)

    elif page == "Predictions":
        show_predictions()

    elif page == "Model Analytics":
        show_model_analytics(results)

    elif page == "Dataset Explorer":
        show_dataset_explorer(df)
