# Evidently AI in Docker 

## 📌 Introduction
This project sets up an **Evidently AI-powered Streamlit dashboard** inside a Docker container. It helps monitor machine learning models by generating interactive reports.

## 📂 Project Structure
```
📁 8-EvidentlyAI
 ├── 📂 projects                # ML monitoring projects
 │    ├── 📂 project_1
 │    │    ├── 📂 reports       # Stores monitoring reports
 │    ├── 📂 project_2
 │    │    ├── 📂 reports
 ├── 📄 app.py                   # Main Streamlit application
 ├── 📄 Dockerfile               # Defines Docker image for Streamlit
 ├── 📄 requirements.txt          # Python dependencies
 ├── 🖼 Screenshot.png            # Screenshot of running app
```

## 🛠 Steps to Run

### 1️⃣ **Build the Docker Image**
```bash
docker build -t evidently-streamlit .
```

### 2️⃣ **Run the Container**
```bash
docker run -p 8501:8501 evidently-streamlit
```

### 3️⃣ **Access the App**
- Open **http://localhost:8501** in your browser.

### 📷 Screenshot
Below is a screenshot of the running Streamlit app:

![Evidently AI Dashboard](Screenshot%202025-03-19%20at%208.13.22%E2%80%AFPM.png)

## 🎯 Features
✅ Loads available projects dynamically.
✅ Allows users to select a project and view reports.
✅ Uses **Evidently AI** to generate insights.
✅ Fully containerized using Docker for easy deployment.

## 🚀 Next Steps
🔹 Add authentication for project access.
🔹 Implement report comparisons over different periods.
🔹 Deploy on a cloud platform (AWS/GCP).

