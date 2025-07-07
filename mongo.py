import pandas as pd
from pymongo import MongoClient

# Load Excel file
excel_file_path = '/home/domie/Documents/Datasets/cancer_patients.xlsx'
df = pd.read_excel(excel_file_path)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['kiruidb']
collection = db['patients']

# Insert data into MongoDB (if not already present)
data_dict = df.to_dict(orient='records')
if data_dict:
    result = collection.insert_many(data_dict)
    print(f"Inserted {len(result.inserted_ids)} documents into the collection.")
else:
    print("No data to insert.")