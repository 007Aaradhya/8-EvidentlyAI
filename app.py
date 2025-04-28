import streamlit as st  
import os  

st.title("Evidently AI - ML Model Monitoring")

# Handle projects directory
project_dir = os.path.join(os.getcwd(), "projects")
try:
    if not os.path.exists(project_dir):
        os.makedirs(project_dir)
        st.info(f"Created projects directory at {project_dir}")

    projects = [p for p in os.listdir(project_dir) 
               if os.path.isdir(os.path.join(project_dir, p))]

    if not projects:
        st.warning("No projects found. Please add project folders in the 'projects' directory.")
        st.stop()

    # Project selection
    project = st.selectbox("Select a project", projects)
    report_dir = os.path.join(project_dir, project, "reports")

    if not os.path.exists(report_dir):
        st.error(f"Report directory not found at {report_dir}")
        st.stop()

    reports = [r for r in os.listdir(report_dir) if r.endswith(".html")]
    
    if not reports:
        st.error("No HTML reports found in the reports directory!")
        st.stop()

    # Report selection and display
    report = st.selectbox("Select a report", reports)
    try:
        with open(os.path.join(report_dir, report), "r") as f:
            st.components.v1.html(f.read(), height=600, scrolling=True)
    except Exception as e:
        st.error(f"Failed to load report: {str(e)}")

except Exception as e:
    st.error(f"An unexpected error occurred: {str(e)}")