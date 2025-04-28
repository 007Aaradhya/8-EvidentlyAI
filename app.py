import streamlit as st  
import os  
import pandas as pd  
import evidently  
from evidently.dashboard import Dashboard  
from evidently.dashboard.tabs import DataDriftTab  

# Streamlit UI
st.title("Evidently AI - ML Model Monitoring")

# Load available projects
project_dir = "projects"
if not os.path.exists(project_dir):
    os.makedirs(project_dir)

projects = [p for p in os.listdir(project_dir) if os.path.isdir(os.path.join(project_dir, p))]

if projects:
    project = st.selectbox("Select a project", projects)
    report_dir = os.path.join(project_dir, project, "reports")

    if os.path.exists(report_dir):
        reports = [r for r in os.listdir(report_dir) if r.endswith(".html")]
        if reports:
            report = st.selectbox("Select a report", reports)
            st.markdown(f"### Report Preview: {report}")
            with open(os.path.join(report_dir, report), "r") as f:
                st.components.v1.html(f.read(), height=600)
        else:
            st.error("No reports found!")
    else:
        st.error("Report directory does not exist!")
else:
    st.error("No projects found!")
