# 📊 CORD-19 Data Explorer

This project is a **Streamlit web application** for exploring the **CORD-19 research dataset** (COVID-19 research papers metadata).  
It demonstrates basic **data analysis, visualization, and web app development** using Python.

---

## 📁 Dataset Information

The original dataset (`metadata.csv`) is very large and cannot be uploaded directly to GitHub.  
Instead, I created a **sample of 2000 rows** for this project to make it manageable.

- **Full dataset**: [CORD-19 on Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)  
- **Sample dataset used here**: `metadata_sample.csv` (2000 random rows)  

The sample ensures the app runs smoothly on **Streamlit Cloud** while still providing meaningful insights.

---


---

## 🚀 Features

1. **Data Loading & Cleaning**
   - Loads `metadata_sample.csv`
   - Converts publication dates
   - Handles missing values

2. **Data Exploration**
   - Shape and structure of dataset
   - Missing value checks
   - Word counts of abstracts

3. **Data Analysis & Visualizations**
   - Publications over time (bar chart)
   - Top journals publishing COVID-19 research
   - Word cloud of paper titles
   - Distribution of papers by source

4. **Interactive Streamlit App**
   - Year range slider
   - Option to show raw data
   - Dynamic visualizations

---

## ▶️ How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/JamesMayen/Frameworks_Assignment.git
   cd Frameworks_Assignment
