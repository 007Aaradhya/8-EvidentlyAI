import streamlit as st
import os
import base64

st.set_page_config(
    page_title="Evidently Report Viewer",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Evidently Report Viewer")

# Add some styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #4B8BBE;
        margin-bottom: 1rem;
    }
    .report-container {
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 1rem;
        background-color: white;
    }
</style>
""", unsafe_allow_html=True)

# Safe path handling
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "projects"))

try:
    # Create projects directory if it doesn't exist
    if not os.path.exists(project_dir):
        os.makedirs(project_dir)
        st.info("Created projects directory. Please add project folders with reports.")
        st.stop()
    
    # List available projects
    projects = [p for p in os.listdir(project_dir)
                if os.path.isdir(os.path.join(project_dir, p))]
    
    if not projects:
        st.warning("No projects found. Add folders to the 'projects' directory.")
        st.stop()
    
    # Create sidebar
    with st.sidebar:
        st.header("Navigation")
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
        
        st.write("---")
        st.markdown("**About**")
        st.info("""
        This application displays Evidently AI reports.
        Select a project and report from the sidebar to view.
        """)
    
    # Main content
    st.header(f"Project: {project}")
    st.subheader(f"Report: {report}")
    
    # Display the report
    with open(os.path.join(report_dir, report), "r", encoding='utf-8') as f:
        html_content = f.read()
        st.components.v1.html(html_content, height=800, scrolling=True)
        
    # Add download button
    def get_binary_file_downloader_html(file_path, file_label='File'):
        with open(file_path, 'rb') as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        return f'<a href="data:application/octet-stream;base64,{b64}" download="{os.path.basename(file_path)}" class="download-button">Download {file_label}</a>'
    
    st.markdown("---")
    st.markdown(get_binary_file_downloader_html(os.path.join(report_dir, report), report), unsafe_allow_html=True)

except Exception as e:
    st.error(f"Error: {str(e)}")
    st.markdown("Please check that your project structure is correct:")
    st.code("""
    project_structure/
    ├── app.py
    ├── requirements.txt
    └── projects/
        ├── project_1/
        │   └── reports/
        │       ├── report1.html
        │       └── ...
        └── project_2/
            └── reports/
                ├── report2.html
                └── ...
    """)