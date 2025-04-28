import streamlit as st  
import os  
import pandas as pd  

# Streamlit UI
st.title("Evidently AI - ML Model Monitoring")

# Load available projects
project_dir = "projects"
try:
    if not os.path.exists(project_dir):
        os.makedirs(project_dir)
        st.info(f"Created projects directory at {project_dir}")

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
                    st.components.v1.html(f.read(), height=600, scrolling=True)
            else:
                st.warning("No reports found in the selected project!")
        else:
            st.warning("No report directory found for this project!")
    else:
        st.info("No projects found. Please add projects to the projects directory.")
        
except Exception as e:
    st.error(f"An error occurred: {str(e)}")