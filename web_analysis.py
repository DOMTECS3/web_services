
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Force TkAgg backend for GUI plots
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

sns.set_theme(style="whitegrid")
warnings.filterwarnings("ignore")


# Read CSV and clean column names
df = pd.read_csv("/home/domie/Downloads/web_services_dataset.csv")
df.columns = df.columns.str.strip()

# Print the first few rows of the DataFrame
print(df.head())
     

# Show each plot in a separate window for clarity
# Status Distribution
if 'status' in df.columns:
    plt.figure(figsize=(8, 6))
    df['status'].value_counts().plot(kind='bar')
    plt.title('Status Distribution')
    plt.xlabel('Status')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()
else:
    print("Column 'status' not found")

# Response Time by Status
if 'status' in df.columns and 'response_time' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='status', y='response_time', data=df)
    plt.title('Response Time by Status')
    plt.xlabel('Status')
    plt.ylabel('Response Time (ms)')
    plt.tight_layout()
    plt.show()



# Response Time Distribution (Histogram)
if 'response_time' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.histplot(df['response_time'], bins=30, kde=True)
    plt.title('Response Time Distribution')
    plt.xlabel('Response Time (ms)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()


# Response Time Boxplot
if 'response_time' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df['response_time'])
    plt.title('Response Time Boxplot')
    plt.xlabel('Response Time (ms)')
    plt.tight_layout()
    plt.show()
    
    