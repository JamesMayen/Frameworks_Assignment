# CORD-19 Data Analysis and Visualization with Streamlit
# This script loads a sample of the CORD-19 dataset, performs basic cleaning,

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import streamlit as st

# ======================
# Part 1: Data Loading
# ======================
@st.cache_data
def load_data():
    df = pd.read_csv("metadata_sample.csv", low_memory=False)  # use the smaller file
    return df

df = load_data()

st.title("CORD-19 Data Explorer")
st.write("A simple exploration of the COVID-19 research papers dataset.")

# Show sample of data
if st.checkbox("Show raw data sample"):
    st.write(df.head())

# Basic info
st.subheader("Dataset Overview")
st.write(f"Shape of dataset: {df.shape}")
st.write("Data Types:")
st.write(df.dtypes)
st.write("Missing Values (first 20 columns):")
st.write(df.isnull().sum().head(20))

# ======================
# Part 2: Data Cleaning
# ======================
st.subheader("Data Cleaning")

# Convert publish_time to datetime
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

# Extract year
df["year"] = df["publish_time"].dt.year

# Abstract word count
if "abstract" in df.columns:
    df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))

# Drop rows with no title or publish_time
df_clean = df.dropna(subset=["title", "publish_time"])

st.write(f"Shape after cleaning: {df_clean.shape}")

# ======================
# Part 3: Analysis & Visualization
# ======================
st.subheader("Data Analysis & Visualization")

# Slider to filter by year range
year_min, year_max = int(df_clean["year"].min()), int(df_clean["year"].max())
year_range = st.slider("Select year range", year_min, year_max, (2020, 2021))

df_filtered = df_clean[(df_clean["year"] >= year_range[0]) & (df_clean["year"] <= year_range[1])]

# 1️⃣ Publications by Year
st.write("### Publications by Year")
year_counts = df_clean["year"].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values, color="skyblue", edgecolor="black")
ax.set_title("Publications per Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# 2️⃣ Top Journals
st.write("### Top Journals Publishing COVID-19 Research")
if "journal" in df_filtered.columns:
    top_journals = df_filtered["journal"].value_counts().head(10)
    fig, ax = plt.subplots()
    sns.barplot(x=top_journals.values, y=top_journals.index, palette="viridis", ax=ax)
    ax.set_title("Top 10 Journals")
    ax.set_xlabel("Number of Papers")
    st.pyplot(fig)

# 3️⃣ Word Cloud of Titles
st.write("### Word Cloud of Paper Titles")
titles = " ".join(df_filtered["title"].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# 4️⃣ Distribution by Source
st.write("### Distribution of Papers by Source")
if "source_x" in df_filtered.columns or "source" in df_filtered.columns:
    source_col = "source_x" if "source_x" in df_filtered.columns else "source"
    source_counts = df_filtered[source_col].value_counts().head(10)
    fig, ax = plt.subplots()
    sns.barplot(x=source_counts.values, y=source_counts.index, palette="coolwarm", ax=ax)
    ax.set_title("Top Sources")
    ax.set_xlabel("Number of Papers")
    st.pyplot(fig)

# ======================
# Part 4: Reflection
# ======================
st.subheader("Reflection")
st.markdown("""
- **Data Cleaning:** Many missing abstracts and journal names, but enough data to analyze.
- **Insights:** Research peaked in 2020–2021. A few journals dominate COVID-19 publishing.
- **Challenges:** Handling missing values and large dataset size.
- **Next Steps:** Try advanced NLP on abstracts or network analysis of authors.
""")

st.write("📌 End of CORD-19 Data Explorer App(James Mayen)")
