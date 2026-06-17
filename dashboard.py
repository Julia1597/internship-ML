import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Data Drift Monitoring Dashboard",
    layout="wide"
)

st.title("Data Drift & Quality Monitoring Dashboard")

st.write("""
This dashboard presents the main outputs of the data drift monitoring project.
It includes drift detection results, data quality checks, and a comparison between
the manual implementation and the automated pipeline.
""")

st.header("1. Drift Detection Results")

drift_file = "drift/drift_results.csv"

if os.path.exists(drift_file):
    drift_df = pd.read_csv(drift_file)
    st.dataframe(drift_df)

    st.subheader("PSI by Variable")

    image_file = "drift/psi_by_variable.png"
    if os.path.exists(image_file):
        st.image(image_file, caption="PSI values by variable with drift thresholds")
    else:
        st.warning("PSI graph not found.")
else:
    st.warning("drift_results.csv not found.")

st.header("2. Data Quality Checks")

quality_file = "drift/data_quality_results.csv"

if os.path.exists(quality_file):
    quality_df = pd.read_csv(quality_file)
    st.dataframe(quality_df)

    st.write("""
    These checks include missing values, duplicated rows and outlier detection.
    """)
else:
    st.warning("data_quality_results.csv not found.")

st.header("3. Manual and Automated Results Comparison")

comparison_file = "output/comparaison/drift_comparaison.csv"

if os.path.exists(comparison_file):
    comparison_df = pd.read_csv(comparison_file)
    st.dataframe(comparison_df)

    st.write("""
    The manual approach gives a global comparison between reference and recent data.
    The automated pipeline gives results for different periods, which makes the monitoring
    more detailed over time.
    """)
else:
    st.warning("drift_comparaison.csv not found.")

st.header("4. Conclusion")

st.write("""
This dashboard gives a simple view of the monitoring outputs. It helps to identify
which variables are stable, which variables show drift, and whether the dataset has
basic quality issues before the analysis.
""")