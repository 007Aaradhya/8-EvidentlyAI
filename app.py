import streamlit as st
import os

st.title("Evidently Report Viewer")

# Safe path handling
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "projects"))

try:
    if not os.path.exists(project_dir):
        os.makedirs(project_dir)
        st.info("Created projects directory")

    projects = [p for p in os.listdir(project_dir) 
               if os.path.isdir(os.path.join(project_dir, p))]
    
    if not projects:
        st.warning("No projects found. Add folders to the 'projects' directory.")
        st.stop()

    project = st.selectbox("Select project", projects)
    report_dir = os.path.join(project_dir, project, "reports")

    if not os.path.exists(report_dir):
        st.error(f"No 'reports' folder in {project}")
        st.stop()

    reports = [r for r in os.listdir(report_dir) if r.endswith(".html")]
    
    if not reports:
        st.error("No HTML reports found")
        st.stop()

    report = st.selectbox("Select report", reports)
    
    with open(os.path.join(report_dir, report), "r") as f:
        st.components.v1.html(f.read(), height=800, scrolling=True)

except Exception as e:
    st.error(f"Error: {str(e)}")