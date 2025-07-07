import pandas as pd

def clean_and_transform(df):
    """Clean and transform the DataFrame."""
    # Example: drop duplicates, fill missing values, convert types
    df = df.drop_duplicates()
    df = df.fillna(method='ffill')
    # Add more transformation logic as needed
    print(f"Transformed data: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

# Example usage (remove or comment out in production):
# df = clean_and_transform(df)
