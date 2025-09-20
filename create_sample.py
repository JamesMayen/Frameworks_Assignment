import pandas as pd
import os

# Path to the original large file
data_path = os.path.join("data", "metadata.csv")   

# Load the full dataset
print("📥 Loading full metadata.csv (this may take a while)...")
df = pd.read_csv(data_path, low_memory=False)

# Show original size
print(f"✅ Original dataset shape: {df.shape}")

# Take a random sample of 2000 rows for quicker analysis
df_sample = df.sample(n=2000, random_state=42)

# Save sample in the main folder for easy access in my Streamlit app
sample_path = "metadata_sample.csv"
df_sample.to_csv(sample_path, index=False)

print(f"🎉 Sample created successfully: {sample_path}")
print(f"📊 Sample dataset shape: {df_sample.shape}")
